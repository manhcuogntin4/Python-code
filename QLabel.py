import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget() 
	
   l1 = QLabel()
   l2 = QLabel()
   l3 = QLabel()
   l4 = QLabel()
	
   l1.setText("Hello World")
   #l4.setText("TutorialsPoint")
   urlLink="<a href=\"http://www.google.com\">'Click this link to go to Google'</a>" 
   l2.setText(urlLink)
   l4.setText(urlLink)
   l1.setAlignment(Qt.AlignCenter)
   l3.setAlignment(Qt.AlignCenter)
   l4.setAlignment(Qt.AlignRight)
   l3.setPixmap(QPixmap("python.png"))
	
   vbox = QVBoxLayout()
   vbox.addWidget(l1)
   vbox.addStretch()
   vbox.addWidget(l2)
   vbox.addStretch()
   vbox.addWidget(l3)
   vbox.addStretch()
   vbox.addWidget(l4)
	
   #l2.setOpenExternalLinks(True)
   #l2.setTextInteractionFlags(Qt.TextBrowserInteraction);
   l2.linkActivated.connect(clicked)
   l4.linkHovered.connect(hovered)
   #l2.setTextInteractionFlags(Qt.TextSelectableByMouse)
   win.setLayout(vbox)
	
   win.setWindowTitle("QLabel Demo")
   win.show()
   sys.exit(app.exec_())
	
def hovered():
   print "hovering"
def clicked():
   print "clicked"
	
if __name__ == '__main__':
   window()