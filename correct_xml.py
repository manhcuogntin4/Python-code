import cv2
import numpy as np
import glob
import imutils
import os
import sys
from string import Template
import subprocess

FOLDER="./xml_v3/"
STR_REX=r'annotation_date'


def readFolder(strFolderName):
	file_list = []
	st=strFolderName+"*.xml"
	for filename in glob.glob(st): #assuming gif
	    file_list.append(filename)
	return file_list

def readFile(filename):
	f=open(filename, 'r')
	lines=f.readlines()
	return lines

def find_index(filename,str):
	first, last, =0,0
	lines_list= readFile(filename)
	for index,line in enumerate(lines_list):
		print line
		if line.find(str)!=-1:
			first=index
			break
	for index,line in enumerate(lines_list):
		if line.find(str)!=-1:
			last=index
	return first, last

def write_file(filename, lines_list, first, last):
	f=open(filename, 'w')
	for index, line in enumerate(lines_list):
		if (index<first or index>=last) and (line.find('path')==-1):
			f.write(line)

file_list=readFolder(FOLDER)
for file in file_list:
	first, last=find_index(file, STR_REX)
	lines=readFile(file)
	print first, last
	write_file(file, lines, first,last)









