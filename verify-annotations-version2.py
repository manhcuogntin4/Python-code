# -*- coding: utf-8 -*-


import numpy
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PIL import Image
import glob
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
IMAGES_FOLDER="nomEpouse/"
ANNOTAIONS_FILE="nomepouse.txt"
class MyDialog(QDialog):
    def __init__(self, image_list, images_annotation, start_position, strFolderName, parent=None):
        super(MyDialog, self).__init__(parent)
        self.images=image_list
        self.i=start_position
        self.annotations=images_annotation
        self.strFolderName=strFolderName

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, self.mQImage)
        painter.end()

    def keyPressEvent(self, QKeyEvent):
        super(MyDialog, self).keyPressEvent(QKeyEvent)
        if QKeyEvent.text()!='q':
			if(self.i<len(self.images)):
				self.cvImage = cv2.imread(self.strFolderName+str(self.i+1)+".bin.png")
        		height, width, byteValue = self.cvImage.shape
        		byteValue = byteValue * width
        		cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        		self.mQImage = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)
        		msg = QMessageBox()
			text=self.annotations[self.i].encode('utf-8')
        		#msg.setText(self.annotations[self.i])
			msg.setText(text)
        		msg.setInformativeText("Image :" +str(self.i))
        		retval = msg.exec_()
        		self.i=self.i+1

        else:
            app.exit(1)

def readFileAnnotations(strFileName):
	print strFileName
	f = open(strFileName, 'r')
	annotations=[]
	for line in f:
		annotations.append(line)
	f.close()
	return annotations

def readFileImages(strFolderName):
	print strFolderName
	image_list = []
	st=strFolderName+"*.png"
	for filename in glob.glob(st): #assuming gif
	    image_list.append(filename)
	return image_list


if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    strFileName=ANNOTAIONS_FILE
    strFolderName=IMAGES_FOLDER
    image_list=readFileImages(strFolderName)
    images_annotation=readFileAnnotations(strFolderName+strFileName)
    start=1
    w = MyDialog(image_list,images_annotation,start, strFolderName)
    w.resize(600, 400)
    w.show()
    app.exec_()
