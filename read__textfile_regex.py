import re
f = open('prenom.txt', 'r')
f_out=open('prenom-out.txt','w')
listprenom=[]
for line in f:
	#index=line.find(':')
	#str=re.findall(r'(\(m\): [A-Z][a-z]* $)', line)
	#str=re.findall(r'\(m\)\s([A-Z][a-z])*\s:', line)
	str=re.findall(r'\(m\)\s[A-Za-z]*\s:|\(f\)\s[A-Za-z]*\s:', line)
	#print str
	if(str):
		print str
		listprenom.append(str[0])
		f_out.write(str[0] +'\n')
f.close()
f_out.close()