import requests
import glob
import sys
import json
import io
import os.path

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
from pandas import DataFrame

FOLDER_NAME="./nom/"
FOLDER_NAME_ANNOT="./books/book-carte-grise/book-noms/"

def readFileImages(strFolderName):
	print strFolderName
	image_list = []
	st=strFolderName+"*.png"
	for filename in glob.glob(st): #assuming gif
	    image_list.append(filename)
	return image_list

def readFileTexts(strFolderName, ls_Annotation_File):
	text_list=[]
	for i in ls_Annotation_File:
		file_text=strFolderName+str(i)+".gt.txt"
		if os.path.isfile(file_text):
			file = open(file_text, 'r')
			for line in file:
				text_list.append(line)
		else:
				text_list.append("deleted")
	return text_list  

ls_ID=readFileImages(FOLDER_NAME)
ls_Annotation_File=list(range(1, len(ls_ID)+1))
ls_nom=readFileTexts(FOLDER_NAME_ANNOT, ls_Annotation_File)
#print len(ls_Annotation_File), len(ls_ID)
df=DataFrame({'File ID':ls_ID,'File_Annotation':ls_Annotation_File, 'Nom':ls_nom})
df.to_excel('Match_ID_File.xlsx', sheet_name='Match_ID_File', index=False)
