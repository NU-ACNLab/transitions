#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p normal
#SBATCH -t 24:00:00
#SBATCH --mem=10G
#SBATCH -J python_caller

module purge
import dcm2niix

DIR = sys.argv[1]
SUB = sys.argv[2]

scan_folders = /projects/b1108/studies/transitions/data/raw/neuroimaging/bids/sourcedata/$DIR* 


for SCAN in scan_folders; do # Whitespace-safe but not recursive.
    OUTPUT = /projects/b1108/studies/transitions2/data/raw/neuroimaging/bids/$SUB/ses-1
    dcm2niix -b, y -z o -w 1 -f %n--%d--s%s--e%e -o $OUTPUT $SCAN
done
