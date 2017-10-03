import sys
import os
from PIL import Image
import random
import glob
import cv2

IMAGES_FOLDER="./"
images_folder=IMAGES_FOLDER

def readFileImages(strFolderName):
    image_list=[]
    st=strFolderName + "*.png"
    print st
    lt=glob.glob(st)
    for k in lt:
    	print k
    	image_list.append(k)
    return image_list
	

#for f in glob.glob("./*.png"):
#	print f
def getPathName(image_path):
	dir_name=os.path.dirname(image_path)
	path_name=os.path.basename(image_path)
	return dir_name,path_name

list_images=readFileImages(images_folder)
#print list_images
for image_path in list_images:
	color_image=cv2.imread(image_path)
	if color_image.shape[2]>1:
		gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
		dir_name,path_name=getPathName(image_path)
		new_gray_image_base="gray"+path_name
		new_gray_image_path=os.path.join(dir_name, new_gray_image_base)
		cv2.imwrite(new_gray_image_path, gray_image)







