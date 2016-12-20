# -*- coding: utf-8 -*-


import numpy
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PIL import Image
import glob





class MyDialog(QDialog):
    def __init__(self, image_list, images_annotation, parent=None):
        super(MyDialog, self).__init__(parent)
        self.images=image_list
        self.i=0
        self.annotations=images_annotation

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, self.mQImage)
        painter.end()

    def keyPressEvent(self, QKeyEvent):
        super(MyDialog, self).keyPressEvent(QKeyEvent)
        if 'n'== QKeyEvent.text():
			if(self.i<len(self.images)):
				self.cvImage = cv2.imread("tt/"+str(self.i+1)+".bin.png")
        		height, width, byteValue = self.cvImage.shape
        		byteValue = byteValue * width
        		cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        		self.mQImage = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)
        		msg = QMessageBox()
        		msg.setText(self.annotations[self.i])
        		msg.setInformativeText("Image :" +str(self.i))
        		retval = msg.exec_()
        		self.i=self.i+1

        else:
            app.exit(1)

def readFileAnnotations():
	f = open('lieu.txt', 'r')
	annotations=[]
	for line in f:
		annotations.append(line)
	f.close()
	return annotations

def readFileImages():
	image_list = []
	for filename in glob.glob('tt/*.png'): #assuming gif
	    image_list.append(filename)
	return image_list


if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    image_list=readFileImages()
    images_annotation=readFileAnnotations()
    w = MyDialog(image_list,images_annotation)
    w.resize(600, 400)
    w.show()
    app.exec_()
