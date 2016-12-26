f = open('listfonts.txt', 'r')
listfonts=[]
for line in f:
 index=line.find(',')
 index1=line.find('&')
 if(index==-1)and(index1==-1):
 	listfonts.append(line)
 position=0
 #print index
 while(index!=-1) and position<len(line) :
 	temp=line[position:index]
 	#print temp
 	listfonts.append(temp)
 	index=line.find(',',index,len(line))
	if(index!=-1):
		position+=index
 index=line.find('&')
 if(index!=-1):
 	listfonts.append(line[index+1:])
for i in listfonts:
	print i
f.close()
