# -*- coding: utf-8 -*-
import glob
import os
import sys


partic_path_dict = {}
'''
    Creates a dictionary of participants and file paths.
            Parameters:
                    a) None
            Returns:
                    none
'''
def list_participants():
    work_dir = "/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/work"
    for partic in os.listdir(work_dir):
        if(partic[0:5] == "sub-t"):
		fpartic = partic.split("-")[1]
        	path = work_dir + "/" + partic + "/ses-1"
        	partic_path_dict[fpartic] = path
        
'''
    Removes participant name from file names. 
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1
            Returns:
                    none
'''
def remove_name(participant, directory):
    for file in os.listdir(directory):
        parts = file.split("--", 1)
        new_name = participant + "--" + parts[-1]
        os.rename(directory + "/" + file, directory + "/" + new_name) 
'''
    Checks for func, beh, anat, and fmap directories
    Creates them, if they do not exist.
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1
            Returns:
                    none
'''
def makedir(participant, directory):
    #check if directories exist, if not, create them
    if(not os.path.exists(directory + "/func/")):
        os.mkdir(directory + "/func/")
    if(not os.path.exists(directory + "/anat/")):
        os.mkdir(directory + "/anat/")
    if(not os.path.exists(directory + "/fmap/")):
        os.mkdir(directory + "/fmap/")
    if(not os.path.exists(directory + "/beh/")):
        os.mkdir(directory + "/beh/")
'''
    Renames files all per the file renaming document from Nina
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1
            Returns:
                    none
'''
def rename_partic(participant, directory): 
    #search using glob on the pattern that Nina in the doc 
    files = glob.glob(directory + "/" + participant + "--FMAP1--GR--?_ph*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_phase1." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    files = glob.glob(directory + "/" + participant + "--FMAP2--GR--?_ph*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_phase2." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    files = glob.glob(directory + "/" + participant + "--FMAP1--GR--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_magnitude1." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    files = glob.glob(directory + "/" + participant + "--FMAP2--GR--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_magnitude2." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    files = glob.glob(directory + "/" + participant + "--MID1--EP_RM--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-mid_run-01_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    files = glob.glob(directory + "/" + participant + "--MID2--EP_RM--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-mid_run-02_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name)  

    #REST1
    files = glob.glob(directory + "/" + participant + "--REST1--EP_RM--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-01_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    #REST2
    files = glob.glob(directory + "/" + participant + "--REST2--EP_RM--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-02_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name)  
    #REST3
    files = glob.glob(directory + "/" + participant + "--REST3--EP_RM--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-03_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    #REST4
    files = glob.glob(directory + "/" + participant + "--REST4--EP_RM--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_task-rest_run-04_bold." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 
    #T1W
    files = glob.glob(directory + "/" + participant + "--T1w--GR--*")
    for file in files:
        parts = file.split(".", 1)
        new_name = "sub-" + participant + "_ses-1_run-1_T1w." + parts[1]
        print(directory + "/" + new_name)
        os.rename(file, directory + "/" + new_name) 

'''
    Moves files to their respective sub folders
            Parameters:
                    a) participant in f1XXXX format
                    b) directory up to and inclduding ses-1
            Returns:
                    none
'''   
def move_to_folders(participant, directory):
    #move functional files
    func_pattern = "sub-"+ participant + "_ses-1_task*"
    func_files = glob.glob(directory + "/" + func_pattern)
    for file in func_files:
        print(file)
        parts = file.split("/")
        os.rename(file, directory + "/func/" + parts[-1])
    #move anatomical files
    anat_pattern = "sub-"+ participant + "_ses-1_run-1_T1w*"
    anat_files = glob.glob(directory + "/" + anat_pattern)
    for file in anat_files:
        print(file)
        parts = file.split("/")
        os.rename(file, directory + "/anat/" + parts[-1])
    #move fmap files
    fmap_files = glob.glob(directory + "/sub*")
    for file in fmap_files:
        print(file)
        parts = file.split("/")
        os.rename(file, directory + "/fmap/" + parts[-1])



def main():
    #asks user to input a directory
    path = input("Please enter the directory, without quotes:\n")
    
    try:
        list_participants()
    except:
        print("Partic dict failed to be created.")
        sys.exit()
    for key, value in partic_path_dict.items():
        remove_name(key, value)
        makedir(key, value)
        rename_partic(key, value)
        move_to_folders(key, value)

    #try:
        #makedir(participant, directory)
        #rename_partic(participant, directory)
        #move_to_folders(participant, directory)
    #except:
        #print("Rename files failed for " + participant)

if __name__ == "__main__":
    main()




