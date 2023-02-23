import subprocess
import sys

directory = sys.argv[1]
participant = sys.argv[2]

scan_folders = glob.glob("/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/sourcedata/" + directory + "/*" )

for scan in scan_folders:
    output_dir = "/projects/b1108/studies/transitions2/data/raw/neuroimaging/bids/" + participant + "/ses-1"
    input_dir = scan
    base_cmd = "dcm2niix -b, y -z o -w 1 -f %n--%d--s%s--e%e -o "
    subprocess.run([base_cmd, output_dir, input_dir])