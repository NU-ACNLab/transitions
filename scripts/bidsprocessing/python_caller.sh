#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p normal
#SBATCH -t 24:00:00
#SBATCH --mem=10G
#SBATCH -J python_caller

#echo python ${1} > return_file.txt

python dicom_to_bids.sh > return_file.txt


