import os
import glob
import json
import shutil

compressed_path = "/projects/b1108/studies/transitions2/data/raw/neuroimaging/bids/sourcedata/"
compressed_files = glob.glob(compressed_path + "*" )


for compressed in compressed_files:
    print(compressed)
    #grabs subject id from compressed file name
    subject = compressed.split("/")[-1][0:5].lower()
    print(subject)

    #unzip/untar into participant dir
    os.makedirs(compressed_path + subject, exist_ok=True)
    shutil.unpack_archive(compressed, compressed_path + subject)

    if(not(os.path.exists(compressed_path + subject + "/" + subject))):
        next_level = glob.glob(compressed_path + subject + "/*")[0]
        dest = compressed_path + subject + "/1"
        os.makedirs(dest, exist_ok=True)
        for file in glob.glob(next_level + "/s*/*"):
            print(file)
            shutil.move(file, dest)
        for folder in glob.glob(compressed_path + subject + "/e*/s*"):
            os.rmdir(folder)
        os.rmdir(glob.glob(compressed_path + subject + "/e*")[0])
    else:
        
        print("You gotta do this one manually: " + subject)



