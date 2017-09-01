from unidecode import unidecode
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

f = open('prenom_new.txt', 'r')
f_out=open('prenom_dict.txt','w')
for line in f:
	#t=unidecode(line)
	u = unicode(line, "utf-8")
	l= remove_accents(u)
	if(l):
		f_out.write(l.upper())

f.close()
f_out.close()