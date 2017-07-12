
import cv2
import numpy as np
import imutils
import os
import glob
from shutil import copyfile


IMAGES="./"

def readFileText(file):
	with open (file, "r") as myfile:
		data=myfile.read()
	return data

def connectFileText(file1, file2,fileout):
	str1= readFileText(file1).strip()
	str2=readFileText(file2).strip()
	file = open(fileout,'w')
	file.write(str1+ " " + str2) 

def connectFileImages(img1_path, img2_path):
	img1 = cv2.imread(img1_path, 0)
	img2 = cv2.imread(img2_path, 0)
	vis = np.concatenate((img1, img2), axis=1)
	#cv2.imwrite('out.png', vis)
	return vis

def readFileImages():
    #print strFolderName
    image_list = []
    #st=strFolderName+"*.png"
    for filename in glob.glob("*.png"): #assuming gif
        image_list.append(filename)
    return image_list

list_file_images=readFileImages()
count=4
for file1 in list_file_images:
	for file2 in list_file_images:
		base1=file1.find(".")
		base1=file1[:base1]
		base2=file2.find(".")
		base2=file2[:base2]
		#print base1, base2, file1, file2
		vis=connectFileImages(file1,file2)
		cv2.imwrite(str(count)+".bin.png", vis)
		connectFileText(base1+".gt.txt", base2+".gt.txt", str(count)+".gt.txt")
		count=count+1



#vis=connectFileImages(path_1,path_2)
#cv2.imwrite("out.png",vis)