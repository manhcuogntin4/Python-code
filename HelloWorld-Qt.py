# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(200,200,800,400)
   b.move(200,200)
   w.setWindowTitle("PyQt")
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()