from hash import hash
import sys



hashing = hash(1000000,4)	

hashing.insertValue('pedro',10)
hashing.insertValue('pedro',20)
hashing.insertValue('pedra',90)
hashing.insertValue('carvalho',50)


print(hashing.getValue('pedro'))
print(hashing.getValue('pedra'))
print(hashing.getValue('carvalho'))