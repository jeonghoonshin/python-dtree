import csv, math

class DataSet:
	""" Data set for samples """

	# attribute types
	NOMINAL = 0
	NUMERIC = 1
	OTHERS = 2

	def __init__(self, csvFilePath = None, metadataFilePath = None):
		""" Initialize a new data set object """
		self.attributes = []
		self.attrTypes = []
		self.data = []	# data points
		self.numData = 0 # number of data points

		self.classAttr = '' # classification attribute

		# load samples
		if csvFilePath and metadataFilePath:
			self.load(csvFilePath, metadataFilePath)

	def __str__(self):
		""" Returns a human readable string representing data set """
		string = ''
		for i, sample in enumerate(self.data):
			string += 'Point ' + str(i) + ': '
			string += str(self.data[i]) + '\n'

		return string

	def load(self, csvFilePath, metadataFilePath):
		""" Loads a csv file and parses its contents into a list with 
		specifications in metadata file"""
		f = open(csvFilePath, 'rb')
		reader = csv.reader(f)
		l = list(reader)

		# extract attributes and data points
		self.attributes = map(lambda x: x.strip(), l[0])
		self.data = l[1:10]

		self.classAttr = self.attributes[-1].strip()

		f = open(metadataFilePath)
		for line in f:
			type = line[line.index(':')+1:].strip()

			# save attribute type
			if type == 'nominal':
				self.attrTypes.append(self.NOMINAL)
			elif type == 'numeric':
				self.attrTypes.append(self.NUMERIC)
			else:
				self.attrTypes.append(self.OTHERS)

		# convert values to correct type
		for i, sample in enumerate(self.data):
			self.numData += 1
			for j, type in enumerate(self.attrTypes):
				val = self.data[i][j]
				if type == self.NUMERIC and val != '?':
					self.data[i][j] = float(val)

	def get_subset(self, subsetIndices = None):
		""" Returns a subset of data points specified by subsetIndices """

		# use whole set if no subset specified
		if subsetIndices is None:
			subsetIndices = range(self.numData)

		subset = DataSet()
		subset.attributes = self.attributes
		subset.attrTypes = self.attrTypes
		subset.classAttr = self.classAttr

		for index in subsetIndices:
			subset.numData += 1
			subset.data.append(self.data[index])

		return subset


	def get_attr_type(self, attr):
		""" Returns attribute type """
		return self.attrTypes[self.attributes.index(attr)]


	def get_values(self, attr):
		""" Returns values under specified attribute """

		# get attribute index
		attrIndex = self.attributes.index(attr)

		# get values but ingnore missing ones
		values = []
		for index in range(self.numData):
			val = self.data[index][attrIndex]
			if val != '?':
				values.append(val)

		return values


	def entropy(self):
		""" Calculates entropy of this data set """

		distribution = {}

		values = self.get_values(self.classAttr)
		numData = len(values)
		for v in values:
			if distribution.has_key(v):
				distribution[v] += 1
			else:
				distribution[v] = 1

		entropy = 0
		for index, key in enumerate(distribution):
			p = distribution[key]/float(numData)
			entropy -= p*math.log(p,2)

		return entropy


	def split(self, attr):
		""" Splits the data set using given non-numeric attribute. 
		Returns a list of DataSet objects after the split """

	def gain(self, attr):
		""" Calculates the gain from splitting with the specified attribute """

		attrType = selg.get_attr_type(attr)
		values = self.get_values(attr)

		if attrType == self.NUMERIC:
			groups = self.splitNumeric(attr, point)
		else:
			groups = self.split(attr)

		return 0

