#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p short
#SBATCH -t 1:00:00
#SBATCH --mem=2G
#SBATCH -J t_nifti

module purge
module load dcm2niix

DIR=$1
SUB=$2

scan_folders = /projects/b1108/studies/transitions/data/raw/neuroimaging/bids/sourcedata/$DIR* 


for SCAN in scan_folders; do # Whitespace-safe but not recursive.
    OUTPUT=/projects/b1108/studies/transitions2/data/raw/neuroimaging/bids/$SUB/ses-1
    dcm2niix -b, y -z o -w 1 -f %n--%d--s%s--e%e -o #$OUTPUT $SCAN
done

#/var/spool/slurmd/job4423074/slurm_script: line 12: DIR: command not found
#/var/spool/slurmd/job4423074/slurm_script: line 13: SUB: command not found
#/var/spool/slurmd/job4423074/slurm_script: line 15: scan_folders: command not found
#/var/spool/slurmd/job4423074/slurm_script: line 19: OUTPUT: command not found
