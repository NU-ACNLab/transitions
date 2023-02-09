import os
import glob
import json
import shutil

##Deal with that we're in an infinite loop
compressed_path = "/projects/b1108/studies/transitions2/data/raw/neuroimaging/bids/sourcedata/"
compressed_files = glob.glob(compressed_path + "*" ) +


for compressed in compressed_files:
    print(compressed)
    #grabs subject id from compressed file name
    subject = compressed.split("/")[-1][0:5].lower()
    print(subject)

    #unzip/untar into participant dir
    os.makedirs(compressed_path + subject, exist_ok=True)
    uncom_path = "/projects/b1108/studies/transitions2/data/raw/neuroimaging/dicoms/uncompressed/"
    shutil.unpack_archive(compressed, uncom_path + subject)

    if(not(os.path.exists(uncom_path + subject + "/" + subject))):
        next_level = glob.glob(uncom_path + subject + "/*")[0]
        dest = uncom_path + subject + "/1"
        os.makedirs(dest, exist_ok=True)
        for file in glob.glob(next_level + "/s*/*"):
            print(file)
            shutil.move(file, dest)
        for folder in glob.glob(uncom_path + subject + "/e*/s*"):
            os.rmdir(folder)
        os.rmdir(glob.glob(uncom_path + subject + "/e*")[0])
    else:

        print("You gotta do this one manually: " + subject)
    com_path = "/projects/b1108/studies/transitions2/data/raw/neuroimaging/dicoms/compressed/"
    shutil.move(compressed, com_path + subject)

    



