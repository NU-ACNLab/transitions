#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p normall
#SBATCH -t 24:00:00
#SBATCH --mem=10G
#SBATCH -J python_caller

python ${1}