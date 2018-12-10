from hash import hash
import sys
import os
import re
import unicodedata
def lerPasta(pasta):
	caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
	return arquivos

def removerAcentosECaracteresEspeciais(palavra):

    palavra = re.sub("[\(\[].*?[\)\]]","",palavra)
    nfkd = unicodedata.normalize('NFKD',palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    palavraSemAcento = palavraSemAcento.replace("\n"," ")
    palavraSemAcento = palavraSemAcento.replace("\t","")
    while palavraSemAcento.find("  ") != -1:
   		palavraSemAcento = palavraSemAcento.replace("  "," ")

    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento).upper()

def gerarIndice(arquivo,num):
	arq = open(arquivo,'rb')
	palavras = arq.read()
	palavas = removerAcentosECaracteresEspeciais(palavras)
	palavras = palavras.split(" ")
	for i in palavras:
		aux = i
		count = palavras.count(aux)
		hashing.insertValue(aux,[count, aux])


hashing = hash(1000000,4,'multiplication','quadratic')	

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

print(hashing.getValue("Agora,"))




