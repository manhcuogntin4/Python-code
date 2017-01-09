# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verify.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VerifyDialog(object):
    def setupUi(self, VerifyDialog, image_list, images_annotation, start_position, strFolderName, parent=None):
        VerifyDialog.setObjectName(_fromUtf8("VerifyDialog"))
        VerifyDialog.resize(681, 519)
        self.images=image_list
        self.i=start_position
        self.annotations=images_annotation
        self.strFolderName=strFolderName
        self.buttonBox = QtGui.QDialogButtonBox(VerifyDialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 450, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(VerifyDialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 300, 611, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.imageEdit = QtGui.QLineEdit(VerifyDialog)
        self.imageEdit.setGeometry(QtCore.QRect(30, 350, 300, 31))
        self.imageEdit.setObjectName(_fromUtf8("imageEdit"))
        self.label = QtGui.QLabel(VerifyDialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 611, 211))
        self.pushButton = QtGui.QPushButton(VerifyDialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 400, 141, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.nextImage)
        self.previousButton = QtGui.QPushButton(VerifyDialog)
        self.previousButton.setGeometry(QtCore.QRect(200, 400, 141, 27))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.previousButton.clicked.connect(self.previousImage)
        self.retranslateUi(VerifyDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VerifyDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VerifyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VerifyDialog)
        text=self.annotations[self.i].encode('utf-8')
        self.lineEdit.setText(text)
        self.imageEdit.setText("Image :" +str(self.i))
	self.label.setPixmap(QtGui.QPixmap(self.strFolderName+str(self.i+1)+".bin.png"))

    def retranslateUi(self, VerifyDialog):
        VerifyDialog.setWindowTitle(_translate("VerifyDialog", "Verify Dialog", None))
        self.pushButton.setText(_translate("VerifyDialog", "Next", None))
        self.previousButton.setText(_translate("VerifyDialog", "Previous", None))
    def nextImage(self):
        if(self.i<len(self.images)):
                self.i=self.i+1
                self.label.setPixmap(QtGui.QPixmap(self.strFolderName+str(self.i+1)+".bin.png"))
                text=self.annotations[self.i].encode('utf-8')
                self.lineEdit.setText(text)
                self.imageEdit.setText("Image :" +str(self.i))
    def previousImage(self):
        if(self.i<len(self.images) and self.i>1):
                self.i=self.i-1
                self.label.setPixmap(QtGui.QPixmap(self.strFolderName+str(self.i+1)+".bin.png"))
                text=self.annotations[self.i].encode('utf-8')
                self.lineEdit.setText(text)
                self.imageEdit.setText("Image :" +str(self.i))
                

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

if __name__ == "__main__":
    import sys
    strFileName=ANNOTAIONS_FILE
    strFolderName=IMAGES_FOLDER
    image_list=readFileImages(strFolderName)
    images_annotation=readFileAnnotations(strFolderName+strFileName)
    start=1
    app = QtGui.QApplication(sys.argv)
    VerifyDialog = QtGui.QDialog()
    ui = Ui_VerifyDialog()
    ui.setupUi(VerifyDialog, image_list,images_annotation,start, strFolderName)
    VerifyDialog.show()
    sys.exit(app.exec_())

