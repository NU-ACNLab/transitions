#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p short
#SBATCH -t 2:00:00
#SBATCH --mem=10G
#SBATCH -J python_caller


python ${1}