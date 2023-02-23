#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p short
#SBATCH -t 1:00:00
#SBATCH --mem=2G
#SBATCH -J t_nifti

module purge
module load dcm2niix

DIR=$1 #check if $ needed. 
echo $DIR
SUB=$2
echo $SUB

scan_folders=/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/sourcedata/$DIR/* 
echo $scan_folders

for SCAN in $scan_folders; do # Whitespace-safe but not recursive.
    echo $SCAN
    OUTPUT=/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/sub-$SUB/ses-1
    echo $OUTPUT
    dcm2niix -b y -z o -w 1 -f %n--%d--s%s--e%e -o $OUTPUT $SCAN
done

#Error: Unknown command line argument: '-b,'
# Error: invalid option '-o (null)'
