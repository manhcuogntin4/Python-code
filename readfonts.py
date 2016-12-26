f = open('listfonts.txt', 'r')
listfonts=[]

for line in f:
 count_virgule=0
 count_and=0
 index=line.find(',')
 index1=line.find('&')
 if(index==-1)and(index1==-1):
 	listfonts.append(line)
 position=index
 first=0
 #print index
 while(index!=-1) and position<len(line) :
 	temp=line[first:position]
 	print first, position
 	print temp
 	count_virgule=count_virgule+1
 	listfonts.append(temp)
 	first=position+1
 	index=line.find(',',position+1,len(line))
 	print index
	if(index!=-1):
		position=index
 index=line.find('&')
 if(index!=-1):
 	listfonts.append(line[index+1:])
 	count_and=count_and+1
 if(count_virgule==0)and(count_and==1):
 	listfonts.append(line[:index])
 if(count_virgule==1)and(count_and==0):
 	listfonts.append(line[position+1:])
 if(count_and==1)and(count_virgule!=0):
 	listfonts.append(line[position+1:index])
file_fonts=open('listfontresult.txt','w')
for i in listfonts:
	file_fonts.write(i+ "\n")
	print i
f.close()
