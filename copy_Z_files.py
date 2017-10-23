import cv2
import numpy as np
import glob
import imutils
import os
import sys
from string import Template
import subprocess
import argparse
from shutil import copyfile
import shutil

#IMAGES_FOLDER="./"

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,
	help="source folder")

ap.add_argument("-d", "--destination", required=True,
	help="destination folder")

args = vars(ap.parse_args())

SOURCE_FOLDER=args["source"]
DEST_FOLDER=args["destination"]


def readFilesFolder(strFolderName):
	print strFolderName
	text_list = []
	st=strFolderName+"*.txt"
	for filename in glob.glob(st): #assuming gif
	    text_list.append(filename)
	return text_list


def readFileText(file):
	with open (file, "r") as myfile:
		data=myfile.read()
		#print data
		index=data.find('Z')
	return index


def copy_file(file,dst):
	text_filename=os.path.basename(file)
	dirname=os.path.dirname(file)
	img_file=text_filename[:text_filename.index('.')]+".bin.png"
	img_file=os.path.join(dirname,img_file)
	shutil.copy2(file, dst)
	shutil.copy2(img_file,dst)

list_files=readFilesFolder(SOURCE_FOLDER)
#print list_files
for file in list_files:
	index=readFileText(file)
	if index>0:
		copy_file(file, DEST_FOLDER)






