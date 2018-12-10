from hash import hash
import unicodedata
import sys
import os
import re

def lerPasta(pasta):
	caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
	return arquivos

def removerAcentosECaracteresEspeciais(palavra):
	nfkd = unicodedata.normalize('NFKD', unicode(palavra))
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def gerarIndice(arquivo,num):
	arq = open(arquivo,'r')
	palavras = arq.read()
	palavras = palavras.replace(",","").replace(".","").replace("!","").replace("?","")
	palavras = palavras.split(" ")
	for i in palavras:
		print(i)
		aux = i
		count = palavras.count(aux)
		print(count,num)
	
		hashing.insertValue(aux,[count, num+1])


hashing = hash(1000000,3,'multiplication','quadratic')	

hashing.insertValue('pedro',10)

hashing.insertValue('pedro',20)
hashing.insertValue('pedra',90)
hashing.insertValue('carvalho',50)


print(hashing.getValue('pedro'))
print(hashing.getValue('pedra'))
print(hashing.getValue('ajoao'))

arquivos = lerPasta('base')
for i in range(len(arquivos)):
	gerarIndice(arquivos[i],i)

print(hashing.getValue("muito"))




