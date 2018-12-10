import math
class content:
	def __init__(self,key,value):
		self.value = []
		self.value.append(value)
		self.key = key




class hash:

	def __init__(self,size,limit, hashMethod="division",colisionMethod = 'linear'):
		self.array = [None] * size
		self.size = size
		self.limit = limit
		self.count = 0
		#design pattern : Strategy
		if hashMethod == 'multiplication':
			self.hash = self.getValueMultiplication
		else:
			self.hash = self.getValueDivision
		#design pattern : Strategy
		if (colisionMethod == 'quadratic'):
			self.colision = self.getQuadraticValue
		else:
			self.colision = self.getLinearValue

		
	def getArray(self):
		return self.array

	def insertValue(self,key,value):
		if(len(key)< self.limit):
			return False
		count = 0
		#get hash code of key
		numericKey = self.hash(key)
		while(True):
			print(numericKey)
			obg = content(key,value)
			# has colision
			if(self.array[numericKey]!= None):
				if(self.array[numericKey].key != key):
					#colision function
					numericKey = self.colision(numericKey,count)
					count = count + 1

				else:
					# if he key already have a value 
					self.array[numericKey].value.append(value)
					break
					
			else:
				self.array[numericKey] = obg
				self.count = count+1
				break

		
		return True


	def getValue(self,key):
		if(len(key)<self.limit):
			return None
		count = 0
		numericKey = self.hash(key)
		if(self.array[numericKey] is None):
			return None
		while(True):
			if(self.array[numericKey] is None):
				return None
			if(self.array[numericKey].key == key):
				return self.array[numericKey].value
			else:
				numericKey = self.colision(numericKey, count)
				count = (count+1)%self.size
		return None

	def getValueDivision(self,key):
		numericKey = 0
		for x in range(0,self.limit):
			numericKey = numericKey + int(ord(key[x]))
		numericKey = int(numericKeyr%len(self.array))
		return numericKey

	def getValueMultiplication(self, key):
		a = (math.sqrt(5)-1)/2
		numericKey = 0
		for x in range(0,self.limit):
			numericKey = numericKey + int(ord(key[x]))

		numericKey = math.floor(math.pow(2,2)*((a*numericKey)%1))
		return int(numericKey)
	def getQuadraticValue(self,key,count):
		index = (key + count*count) % self.size
		return index

	def getLinearValue(self,key,adictionator):
		return int((key+adictionator)%self.size)





