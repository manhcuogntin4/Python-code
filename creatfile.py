f = open('listfonts.txt', 'r')
i=0
for line in f:
 i=i+1
 f1=open(str(i)+".gt.txt",'w')
 f1.write(line)
f.close()
