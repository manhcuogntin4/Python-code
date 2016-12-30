
from subprocess import call
import os
import subprocess
#Open file Annotation and read to vector
lsAnnotaiton=[]
fAnnotation=open("prenoms.txt",'r')
for index,line in enumerate(fAnnotation):
	lsAnnotaiton.append(line)
#Open bad annotaions file and read to vector
fBad=open("mauvais.txt",'r')
lsBad=[]
for line in fBad:
	lsBad.append(int(line)+1)
i=0
#Write to good file annotations
fGood=open("good.txt",'w')

while i<len(lsAnnotaiton):
	if not (i in lsBad):
		fGood.write(lsAnnotaiton[i-1])
	else:
		cmd= "rm " + str(i)+".bin.png"
		os.system(cmd)
	i=i+1
fBad.close()
fAnnotation.close()
fGood.close()



