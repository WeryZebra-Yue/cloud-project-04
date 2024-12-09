#!/bin/bash
#SBATCH --job-name=proj04
#SBATCH --output=output.log
#SBATCH --error=error.log
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=01:00:00

module load python
srun python tspMOD.py --seed 452 --batches 1
