import paramiko

def fetch_and_run_on_owens(weight_type, initial_guess_pickle, random_seed, num_of_trys):
    owens_host = "owens.osc.edu"  # Replace with Owens login hostname
    owens_username = "w029hrp"    # Replace with your Owens username
    owens_password = "erytExan6erytExan6"  # Replace with your Owens password
    database_file_path = "/users/PWSU0471/nehrbajo/proj03data/database00.txt"  # Replace with actual path on Owens
    tsp_script_path = "/users/PWSU0510/w029hrp/workflow/tspMod.py"  # Replace with actual tspMod.py path
    initial_guess_path = f"/users/PWSU0510/w029hrp/workflow/initialGuess.pickle"  # Ensure the pickle file path is correct

    try:
        # Connect to Owens
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(owens_host, username=owens_username, password=owens_password)

        # Fetch best distance from the database
        fetch_cmd = f"cat {database_file_path} | grep 'Best Distance:' | awk '{{print $3}}'"
        stdin, stdout, stderr = ssh.exec_command(fetch_cmd)
        best_distance = stdout.read().decode().strip()
        if not best_distance:
            best_distance = "NA"

        # Ensure the initial guess file exists
        check_pickle_cmd = f"ls {initial_guess_path}"
        stdin, stdout, stderr = ssh.exec_command(check_pickle_cmd)
        if stderr.read():
            raise FileNotFoundError(f"Initial guess file '{initial_guess_pickle}' not found on Owens.")

        # Run tspMod.py with the specified arguments
        run_tsp_cmd = (
            f"python3 {tsp_script_path} {weight_type} {initial_guess_path} {random_seed} {num_of_trys}"
        )
        stdin, stdout, stderr = ssh.exec_command(run_tsp_cmd)
        output = stdout.read().decode()
        error = stderr.read().decode()

        ssh.close()

        if error:
            raise Exception(f"Error while running tspMod.py: {error}")

        return best_distance, output
    except Exception as e:
        return None, str(e)
