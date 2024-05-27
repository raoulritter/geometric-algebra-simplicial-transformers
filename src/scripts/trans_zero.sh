#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gpus=1
#SBATCH --job-name=our_gatr
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=18
#SBATCH --time=06:10:10
#SBATCH --output=model_edges_zeros_%A.out


module purge
module load 2022
module load Anaconda3/2022.05

# Your job starts in the directory where you call sbatch
# Activate your environment
source activate cgest_env
cd ..
srun python main.py --zero_edges
