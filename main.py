# -*- coding: utf-8 -*-
from hash import hash
import unicodedata
import sys
import os
import re
import time

def lerPasta(pasta):
	caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
	return arquivos

def gerarIndice(arquivo,num,hashing):
	arq = open(arquivo,'r')
	palavras = arq.read()
	arq.close()
	palavras = palavras.lower()
	palavras = palavras.replace(",","").replace(".","").replace("!","").replace("?","").replace("\r","").replace("\t","").replace("\n","")

	palavras = palavras.split(" ")
	#print(palavras)
	for i in palavras:
		aux = i
		count = palavras.count(aux)
		flag = True
		if hashing.getValue(aux):
			for k in hashing.getValue(aux):
				if k[0] == count and k[1]== num+1:
					flag = False
			if flag:
				hashing.insertValue(aux,[count, num+1])
		else:
			hashing.insertValue(aux,[count, num+1])

hashingMQ = hash(1000000,3,'multiplication','quadratic')
hashingML = hash(1000000,3,'multiplication')
hashingDQ = hash(1000000,3)	
hashingDL = hash(1000000,3,"division","linear")		



inicio = time.time()
arquivos = lerPasta('base')
for i in range(len(arquivos)):
	gerarIndice(arquivos[i],i,hashingML)

for i in sorted(hashingML.getKeys()):
	#print(hashing.getValue(i)[0])
	print(i,hashingML.getValue(i)[0][0], arquivos[(hashingML.getValue(i)[0][1])-1])

fim = time.time()
print('tempo para Hashing ultilizando metodo da multiplicacao e colizao linear :',fim - inicio)

inicio = time.time()
arquivos = lerPasta('base')
for i in range(len(arquivos)):
	gerarIndice(arquivos[i],i,hashingMQ)

for i in sorted(hashingMQ.getKeys()):
	#print(hashing.getValue(i)[0])
	print(i,hashingMQ.getValue(i)[0][0], arquivos[(hashingMQ.getValue(i)[0][1])-1])

fim = time.time()
print('tempo para Hashing ultilizando metodo da multiplicacao e colizao Quadratica :',fim - inicio)

inicio = time.time()
arquivos = lerPasta('base')
for i in range(len(arquivos)):
	gerarIndice(arquivos[i],i,hashingDL)

for i in sorted(hashingDL.getKeys()):
	#print(hashing.getValue(i)[0])
	print(i,hashingDL.getValue(i)[0][0], arquivos[(hashingDL.getValue(i)[0][1])-1])

fim = time.time()
print('tempo para Hashing ultilizando metodo da Divisao e colizao linear :',fim - inicio)

inicio = time.time()
arquivos = lerPasta('base')
for i in range(len(arquivos)):
	gerarIndice(arquivos[i],i,hashingDQ	)

for i in sorted(hashingDQ.getKeys()):
	#print(hashing.getValue(i)[0])
	print(i,hashingDQ.getValue(i)[0][0], arquivos[(hashingDQ.getValue(i)[0][1])-1])

fim = time.time()
print('tempo para Hashing ultilizando metodo da Divisao e colizao Quadratica :',fim - inicio)


# print(len(hashingML.getKeys()))




while True:
	palavra = input("digite uma palvra:\n")
	print(hashingML.getValue(palavra))



