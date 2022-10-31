# -*- coding: utf-8 -*-
import os
import shutil

'''
    Copies transitions participants from /data/Georgia to /studies
            Parameters:
                    none
            Returns:
                    none
'''
def mover():
    work_dir = "/projects/b1108/data/Georgia/transitions/"
    for partic in os.listdir(work_dir):
        try:
            if(partic[0:5] == "sub-t"):
                for ses in os.listdir(work_dir + partic):
                wd = work_dir + partic + "/" + ses
                    for folder in os.listdir(wd): 
                    #checks to make sure it's a participant
                        source = wd + folder
                        if(folder == "beh"):
                            dest = "/projects/b1108/studies/transitions/data/raw/neuroimaging/behavioral/"\
                                + partic + "/" + ses + "/" + folder
                            shutil.copytree(source, dest) 
                        else:
                            dest = "/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/"\
                                + partic + "/" + ses + "/" + folder
                            shutil.copytree(source, dest) 
                print("Copied succesfully: " + partic)
        except:
            print("FAILED: " + partic)


def main():   
    mover()


if __name__ == "__main__":
    main()