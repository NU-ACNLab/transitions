#!/usr/bin/bash

#SBATCH -A p31833
#SBATCH -p normal
#SBATCH -t 4:00:00
#SBATCH --mem=64G
#SBATCH -J bidskit_sourcedata

module load dcm2niix
bidskit -d /projects/b1108/studies/transitions/data/raw/neuroimaging/bids


