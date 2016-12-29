f = open('listfonts.txt', 'r')
f_out=open('listfonts-out.txt','w')
listfonts=[]
for line in f:
	index=line.find(':')
	if(index != -1):
		listfonts.append(line[index+1:])
		f_out.write(line[index+1:] +'\n')
f.close()
f_out.close()

