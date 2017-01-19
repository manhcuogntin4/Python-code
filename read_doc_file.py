

from docx import Document
from docx.shared import Inches
f = open('demo.docx', 'rb')
document = Document(f)
for a,i in enumerate (f):
	f_out=open(str(a)+".txt", "w")
	f_out.write(i.encode('utf8'))
	f_out.close()
f.close()