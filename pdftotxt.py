import pyPdf
import glob
for filename in glob.glob("data/*.pdf"):
	pdf= pyPdf.PdfFileReader(open(filename, "rb"))
	index=filename.index("/")
	filename=filename[index+1:]
	index=filename.index(".")
	filename=filename[:index]
	for num, page in enumerate(pdf.pages):
	    text= page.extractText().encode('utf8')
	    f=open(filename+str(num)+".txt", "w")
	    f.write(text)
	    f.close()
