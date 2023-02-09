import os
import glob
import json

subjectsPath = "/projects/b1108/studies/transitions/data/raw/neuroimaging/bids/sub-*"
subjects = glob.glob(subjectsPath)


for subject in subjects:
	print(subject)
	#Edit 'ses-1' to be the same as your session
	fmapsPath = os.path.join(subject, 'ses-1', 'fmap', '*.json')
	fmaps = glob.glob(fmapsPath)
	funcsPath = os.path.join(subject, 'ses-1', 'func', '*.nii.gz')
	funcs = glob.glob(funcsPath)

	#substring to be removed from absolute path of functional files
	pathToRemove = subject + '/'
	funcs = list(map(lambda x: x.replace(pathToRemove, ''), funcs))
	for fmap in fmaps:
		with open(fmap, 'r') as data_file:
			fmap_json = json.load(data_file)
		fmap_json['IntendedFor'] = funcs

		with open(fmap, 'w') as data_file:
			fmap_json = json.dump(fmap_json, data_file)
			
