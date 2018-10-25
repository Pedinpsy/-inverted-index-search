class content:
	def __init__(self,key,value):
		self.value = []
		self.value.append(value)
		self.key = key

class hash:
	def __init__(self,size,limit):
		self.array = [None] * size
		self.size = size
		self.limit = limit
		self.count = 0

	def getArray(self):
		return self.array

	def insertValue(self,key,value):
		if(len(key)< self.limit):
			return False
		count = 0
		while(True):
			numericKey = self.getNumericKey(key,count)
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
		while(True):
			if(self.array[self.getNumericKey(key,count)].key == key):
				return self.array[self.getNumericKey(key,count)].value
			else:
				count = count+1
		return None

	def getNumericKey(self,key,adictionator):
		numericKey = 0
		for x in range(0,self.limit):
			numericKey = numericKey + int(ord(key[x]))
		numericKey = int(numericKey+adictionator%len(self.array))
		return numericKey