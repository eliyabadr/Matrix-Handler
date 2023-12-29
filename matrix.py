class matrix:
	def __init__(self, values):
		#self.rows = rows
		#self.columns = columns
		self.values = values
	def getSize(self):
		rows = len(self.values)
		columns = len(self.values[0])
		
		return str(rows) + " x " + str(columns)
	def getValues(self):
		for i in range(len(self.values)):
			print(self.values[i])
		
	def __add__(self, other):
		if self.getSize() != other.getSize():
			print("Cannot add")
		else:
			new_matrix = []
			for i in range(len(self.values)):
				row = []
				for j in range(len(self.values[i])):
					row.append(self.values[i][j] + other.values[i][j])
				new_matrix.append(row)

			result = matrix(new_matrix)
			return result.getValues() 
		
	def findTranspose(self):
		new_matrix = []
		for i in range(len(self.values[0])):
			row = []
			for j in range(len(self.values)):
				row.append(self.values[j][i])
			new_matrix.append(row)	
			
		new_mat = matrix(new_matrix)
		new_mat.getValues()
	def isSquare(self):
		if len(self.values) ==  len(self.values[0]):
			return True
		else:
			return False
	def multiplyByConstant(self, k):
		for i in range(len(self.values)):
			for j in range(len(self.values[i])):
				self.values[i][j] = self.values[i][j] * k
		self.getValues()