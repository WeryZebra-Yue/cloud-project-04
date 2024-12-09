import paramiko
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from threading import Thread
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from regex import regex as re
# Mock database to track the jobs
jobs_db = {}

owens_host = "owens.osc.edu"
owens_username = "w029hrp"
owens_password = "erytExan6erytExan6"
database_file_path = "/users/PWSU0471/nehrbajo/proj03data/database00.txt"
tsp_script_path = "/users/PWSU0510/w029hrp/workflow/tspMod.py"
initial_guess_path = f"/users/PWSU0510/w029hrp/workflow/initialGuess.pickle"

def extract_best_distance(text):
    """
    Extracts the best distance from the text.
    """
    try:
        pattern = r'(\d+)(?=\n\s*\[)'
        best_distances = re.findall(pattern, text)
        best_distance = best_distances[-1] if best_distances else None
    except:
        best_distances = None
        print("No best distances found")
    return best_distance


from .models import Job


def fetch_and_run_on_owens(weight_type, initial_guess_pickle, random_seed, num_of_tries, job_id):
    """
    Function to run calculations on Owens cluster. Used for backend logic.
    """

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(owens_host, username=owens_username, password=owens_password)

        run_tsp_cmd = f"python3 {tsp_script_path} {weight_type} {initial_guess_path} {random_seed} {num_of_tries}"
        print(f"Running command: {run_tsp_cmd}")
        stdin, stdout, stderr = ssh.exec_command(run_tsp_cmd)
        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()
        if error:
            print(f"Error while running tspMod.py: {error}")
            raise Exception(error)

        if output:
            pattern = r'BEST_\d+: (\d+)'
            best_distance = re.findall(pattern, output)[-1]

            # Fetch job from database and update
            job = Job.objects.get(job_id=job_id)
            job.best_distance = best_distance
            job.job_status = "completed"
            job.save()

            print(f"Best distance: {best_distance}")
            return best_distance, output
        return None, None

    except Exception as e:
        print(f"Exception: {str(e)}")
        return None, str(e)

@csrf_exempt
def start_job(request):
    """
    Handles starting the job.
    Starts job logic and returns a unique job ID.
    """
    if request.method == "POST":
        try:
            weight_type = request.POST.get("weight_type", "00")
            random_seed = int(request.POST.get("random_seed", "0"))
            num_of_tries = int(request.POST.get("num_of_tries", "1000000"))

            # Generate a unique job ID
            job_id = f"{weight_type}_{random_seed}_{num_of_tries}"

            # Check if job already exists in database
            if Job.objects.filter(job_id=job_id).exists():
                # if the job has completed, if it is running then run again.
                if Job.objects.get(job_id=job_id).job_status != "completed":
                    # Run job asynchronously
                    thread = Thread(
                        target=fetch_and_run_on_owens,
                        args=(weight_type, "initialGuess.pickle", random_seed, num_of_tries, job_id)
                    )
                    thread.start()
                    # update the job status to running
                    job = Job.objects.get(job_id=job_id)
                    job.job_status = "running"
                    job.save()
                
                return JsonResponse({"status": "success", "job_id": job_id})

            # save the job in the database
            job = Job(
                job_id=job_id,
                weight_type=weight_type,
                random_seed=random_seed,
                num_of_tries=num_of_tries,
                job_status="running",
            )
            job.save()
            # Run job asynchronously
            thread = Thread(
                target=fetch_and_run_on_owens,
                args=(weight_type, "initialGuess.pickle", random_seed, num_of_tries, job_id)
            )
            thread.start()

            return JsonResponse({"status": "success", "job_id": job_id})
        except Exception as e:
            print(f"Error starting job: {e}")
            return JsonResponse({"status": "error", "error": str(e)})

@csrf_exempt
def stop_job(request, job_id):
    """
    Stops a SLURM job on Owens using the job_id sent to the server.
    """
    try:
        # Stop job via SLURM on Owens
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(owens_host, username=owens_username, password=owens_password)

        # cancel the command
        # send the ctrl c command to stop the job
        # Update database entry
        job = Job.objects.get(job_id=job_id)
        job.job_status = "stopped"
        job.save()

        stop_command = f"pkill -f tspMod.py"
        stdin, stdout, stderr = ssh.exec_command(stop_command)
        error = stderr.read().decode()

        ssh.close()

        if error:
            return JsonResponse({"status": "error", "message": error}, status=500)

        

        return JsonResponse({"status": "success", "message": f"Stopped job with ID {job_id}"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

def update_job_status(request, job_id):
    """
    Provides the current job's status to the frontend.
    """
    try:
        job = Job.objects.get(job_id=job_id)
        return JsonResponse({
            "status": job.job_status,
            "best_distance": job.best_distance
        })
    except Job.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Job not found"})

def index(request):
    """
    This view renders the index (home) page.
    """
    return render(request, 'index.html')



# Update Best Distance Logic
@csrf_exempt
def update_best_score(request):
    """
    Fetch the best distance score from the database.
    """
    try:
        # SSH into the server to fetch data from database file
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(owens_host, username=owens_username, password=owens_password)

        # Query to fetch the latest "best distance"
        fetch_cmd = f"cat {database_file_path}"
        stdin, stdout, stderr = ssh.exec_command(fetch_cmd)
        text = stdout.read().decode().strip()
        best_distance = extract_best_distance(text)
        print(f"Best distance: {best_distance}")
        if not best_distance:
            best_distance = "NA"

        ssh.close()

        return JsonResponse({"status": "success", "best_distance": best_distance})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

def best_distance_by_weight_type(request, weight_type):
    """
    Fetch the best distance from the database for a given weight type.
    The latest result is fetched based on timestamp.
    """
    try:
        # Query the database to find the latest best distance for the given weight_type
        result = (
            Job.objects.filter(weight_type=weight_type)
            .order_by("best_distance")
            .first()
        )

        # If a result is found, return it; otherwise, return 'NA'
        if result and result.best_distance:
            # return result.best_distance
            return JsonResponse({
                "status": "success",
                "best_distance": result.best_distance,
            })
            print(f"Best distance: {result.best_distance}")
        return JsonResponse({"status": "not_found", "best_distance": "NA"})
    except Exception as e:
        print(f"Error fetching from database: {e}")
        return "NA"
