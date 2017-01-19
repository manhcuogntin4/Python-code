import pyPdf
import glob
import os.path
save_path="output/"
for filename in glob.glob("data/*.pdf"):
	pdf= pyPdf.PdfFileReader(open(filename, "rb"))
	index=filename.index("/")
	filename=filename[index+1:]
	index=filename.index(".")
	filename=filename[:index]
	for num, page in enumerate(pdf.pages):
	    text= page.extractText().encode('utf8')
	    save_file_path=os.path.join(save_path, filename+str(num)+".txt")
	    f=open(save_file_path, "w")
	    f.write(text)
	    f.close()
