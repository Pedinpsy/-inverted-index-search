import math
class content:
	def __init__(self,key,value):
		self.value = []
		self.value.append(value)
		self.key = key




class hash:

	def __init__(self,size,limit, method="division"):
		self.array = [None] * size
		self.size = size
		self.limit = limit
		self.count = 0
		if method == 'multiplication':
			self.hash = self.getValueMultiplication
		else:
			self.hash = self.getValueDivision

	def getArray(self):
		return self.array

	def insertValue(self,key,value):
		if(len(key)< self.limit):
			return False
		count = 0
		while(True):
			numericKey = self.hash(key,count)
			print(numericKey)
			obg = content(key,value)
			if(self.array[numericKey]!= None):
				if(self.array[numericKey].key != key):
					count = count + 1
				else:
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
		if(self.array[self.hash(key,count)] == None):
			return None
		while(True):


			if(self.array[self.hash(key,count)].key == key):
				return self.array[self.hash(key,count)].value
			else:
				count = count+1
		return None

	def getValueDivision(self,key,adictionator):
		numericKey = 0
		for x in range(0,self.limit):
			numericKey = numericKey + int(ord(key[x]))
		numericKey = int(numericKey+adictionator%len(self.array))
		return numericKey

	def getValueMultiplication(self, key, adictionator):
		adictionator = adictionator+1
		a = (math.sqrt(5)-1)/2
		numericKey = 0
		for x in range(0,self.limit):
			numericKey = numericKey + int(ord(key[x]))

		numericKey = math.floor(adictionator*((a*numericKey)%1))
		return numericKey




