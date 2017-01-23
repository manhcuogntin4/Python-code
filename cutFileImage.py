# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyclstm
from PIL import Image
import sys, getopt
import os
import difflib
from collections import namedtuple
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
INCREASE=False
def readFieldString(st):
	lsField=[]
	for word in st.split():
		lsField.append(word)
	return lsField

def readFileBox(file_name):
	lsLine=[]
	try:
		fBoxFile=open(file_name, "r")
		for line in fBoxFile:
			lsLine.append(line)
	except IOError:
		print "File not found"
	else:
		fBoxFile.close()
	return lsLine

def getCoordinationVector(file_name):
	lsLine=readFileBox(file_name)
	i=0
	lsBoxCoordination=[]
	for line in lsLine:
		BoxCoordination=[]
		if i%2==0: #First line
			firstLine=readFieldString(line)
			BoxCoordination.append(firstLine[1])
			BoxCoordination.append(firstLine[2])
			BoxCoordination.append(firstLine[3])
			BoxCoordination.append(firstLine[4])
		else:
			secondLine=readFieldString(line)
			BoxCoordination.append(secondLine[0])
			BoxCoordination.append(secondLine[1])
			BoxCoordination.append(secondLine[2])
		lsBoxCoordination.append(BoxCoordination)
		i+=1
	return lsBoxCoordination


def mixNearRegion(lsBoxCoordination):
	lsCordination=[]
	isIncrease=INCREASE
	i=0
	for item in lsBoxCoordination:
		if(i<len(lsBoxCoordination)-1):
			if int(lsBoxCoordination[i+1][0])>int(lsBoxCoordination[i][0]) :
				if isIncrease==False:
					lsCordination.append(int(item[0]))
					lsCordination.append(int(item[1]))
					lsCordination.append(int(item[2]))
					lsCordination.append(int(item[3]))
					print lsBoxCoordination[i][0] , lsBoxCoordination[i+1][0] , isIncrease
					isIncrease=True
			else :
				lsCordination.append(int(item[0]))
				lsCordination.append(int(item[1]))
				lsCordination.append(int(item[2]))
				isIncrease=False

		i=i+1

	return lsCordination

def cutFileImage(imageFile, lsCordination):
	img = cv2.imread(imageFile,0)
	height, width = img.shape[:2]
	t2=height
	for i in range(len(lsCordination)/7):
		xMin=lsCordination[7*i]
		yMin=lsCordination[7*i+1]
		yMax=lsCordination[7*i+3]
		xMax=lsCordination[7*i+6]
		print xMin, xMax
		#yMax=lsCordination[6*i+7]
		#print height, width, yMin, height-yMin, height-yMax, xMax
		#image_temps=img[yMin:30, xMin:xMax-xMin]
		image_temps=img[height-yMax:height-yMin, xMin:xMax]
		#t2=yMin
		strTemp="line"+ str(i) + imageFile
		cv2.imwrite(strTemp,image_temps)


st=getCoordinationVector("test1.box")
print st
ls=mixNearRegion(st)
print ls
cutFileImage("test1.tif",ls)
#f=getCoordinationVector("test.box")
#print f

FILE_BOX=""
FILE_IMAGE=""
boxFile=FILE_BOX
imageFile=FILE_IMAGE
#fBoxFile=open(boxFile, "r")
#fImage=cv2.imread(imageFile,1)
BoxCoordination = namedtuple("BoxCoordination", "Box_xMin image_width_1 Box_yMin image_height_1 padding_1 Box_xMax image_width_2 Box_yMax image_height_2 padding_2")
#for line in boxFile:


