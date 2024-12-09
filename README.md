# Project Overview

This project serves as a user interface (UI) for managing computations and processes on the Owens High-Performance Computing (HPC) cluster. The project enables users to:

1. **Start a Job**: Run a computation with specified parameters.
2. **Stop a Job**: Terminate an ongoing computation.
3. **Update Best Distance**: Refresh the best result found so far based on the current weight type.
4. **Monitor Status**: View the status of running jobs and results in real-time.

The project is built using Django for the backend and HTML/JavaScript for the frontend.

---

## Features

### UI Elements
1. **Dropdown**: Select the weight type (default: `00`).
2. **Input Fields**:
   - **Random Seed**: Integer value between 0 and 32000 (default: `0`).
   - **#OfTrys**: Number of tries, must be greater than 0 (default: `1000000`).
   - **#OfBatchJobs**: Number of batch jobs, must be greater than 0 (default: `1`).
3. **Text Boxes**:
   - Display the best distance for the selected weight.
   - Show the job status (e.g., `none submitted`, `running job N of M`, `all complete`).
4. **Buttons**:
   - **Start/Stop**: Toggle between starting and stopping a computation.
   - **Update**: Refresh the displayed best distance.
   - **Reset**: Reset all fields and terminate all jobs if applicable.

### Backend Logic

1. **Start Job**:
   - Accepts input parameters from the UI.
   - Connects to Owens via SSH using `paramiko`.
   - Executes the computation script (`tspMod.py`) with the provided parameters.

2. **Stop Job**:
   - Terminates ongoing computations using either `pkill` or a `STOP` signal file.
   - If the job has not started, cancels it preemptively.

3. **Update Best Distance**:
   - Fetches the latest best distance from the Owens database.

4. **Reset**:
   - Resets UI fields to their initial values.
   - Kills all ongoing jobs on Owens if applicable.

---

## Backend Implementation

### Functions
1. **`fetch_and_run_on_owens(weight_type, random_seed, num_of_trys)`**:
   - Connects to Owens via SSH.
   - Runs `tspMod.py` with the provided parameters.
   - Fetches the best distance from the database.

2. **`stop_all_processes_on_owens()`**:
   - Terminates all processes related to `tspMod.py`.
   - Uses either `pkill` or a `STOP` signal to halt computations.

3. **`create_stop_signal_on_owens()`**:
   - Creates a file (`STOP`) on Owens to signal computations to terminate gracefully.

4. **`update_best_distance(weight_type)`**:
   - Fetches and displays the best distance for the selected weight from the Owens database.

---

## Deployment

1. **Requirements**:
   - Python 3.x
   - Django
   - `paramiko` for SSH connections
   - Owens HPC credentials

2. **Steps**:
   - Clone the repository.
   - Set up a virtual environment and install dependencies using `pip`.
   - Run the Django server using:
     ```bash
     python manage.py runserver
     ```
   - Access the application at `http://localhost:8000/`.

---

## How It Works

### Starting a Job
1. Select parameters from the UI.
2. Click **Start**.
3. The backend connects to Owens and runs `tspMod.py`.
4. Outputs are displayed in the status box.

### Stopping a Job
1. Click **Stop**.
2. The backend sends a command to terminate all relevant processes on Owens.

### Updating Best Distance
1. Select the weight type.
2. Click **Update**.
3. The backend fetches the best distance from the database and displays it in the UI.

---

## Notes
- Ensure the Owens credentials and file paths are correct.
- `tspMod.py` should handle the `STOP` signal file if you choose to implement graceful termination.
- All actions are logged for debugging purposes.

---

## Future Enhancements
- Add authentication for secure access.
- Implement job queuing and priority management.
- Include error handling for edge cases like network failures.

