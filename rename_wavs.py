import glob
import os

dir = "dataset1/"
for i,file in enumerate(glob.glob(dir+"*.wav")):
	name = file.split("/")[-1]
	name = name.split(".")[0]
	os.rename(file,'{}.wav'.format(i))


