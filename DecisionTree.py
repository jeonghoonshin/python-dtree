import csv
import math

class DataSet:
	""" Data set for samples """

	# attribute types
	NOMINAL = 0
	NUMERIC = 1
	OTHERS = 2

	def __init__(self, csvFilePath = None, metadataFilePath = None):
		""" Initialize a new data set object """
		self.dataFile = None
		self.data = {}	# data points
		self.classification = '' # classification attribute
		self.unclassified = []  # list of indices of unclassified instances in dataset

		# load samples
		if csvFilePath and metadataFilePath:
			self.load(csvFilePath, metadataFilePath)

	def load(self, csvFilePath, metadataFilePath):
		""" Loads a csv file and parses its contents into a list with 
		specifications in metadata file"""
		f = open(csvFilePath, 'rb')
		reader = csv.reader(f)
		self.dataFile = reader
		l = list(reader)

		# extract attributes and data points
		attributes = l[0]
		samples = l[1:]

		self.classification = attributes[-1].strip()

		f = open(metadataFilePath)
		attributeType = []
		for line in f:
			type = line[line.index(':')+1:].strip()

			# save attribute type
			if type == 'nominal':
				attributeType.append(self.NOMINAL)
			elif type == 'numeric':
				attributeType.append(self.NUMERIC)
			else:
				attributeType.append(self.OTHERS)

		# construct data dictionary
		for index, attr in enumerate(attributes):
			type = attributeType[index]
			dataPoints = []
			for s in samples:
				dataPoints.append(s[index].strip())
				#if len(dataPoints) == 10: break

			self.unclassified = range(len(dataPoints))

			key = attr.strip()
			value = {'dataType': type, \
							 'dataPoints': dataPoints}

			self.data[key] = value

		self.convert_attr()

	def convert_attr(self):
		""" Converts attribute values based on data type """
		for attr in self.data:
			dataType = self.data[attr]['dataType']
			dataPoints = self.data[attr]['dataPoints']

			func = None
			if dataType == self.NUMERIC:
				func = float

			if func:
				for index, d in enumerate(dataPoints):
					if d != '?':
						dataPoints[index] = float(d)

			return True

	def entropy(self):
		""" Calculates entropy of current data set """
		classifications = self.data[self.classification]['dataPoints']
		numData = len(classifications)
		classDist = {}
		for c in classifications:
			if classDist.has_key(c):
				classDist[c] += 1
			else:
				classDist[c] = 1

		entropy = 0
		for index, key in enumerate(classDist):
			p = classDist[key]/float(numData)
			entropy -= p*math.log(p,2)

		return entropy

	def gain(self, data, attribute):
		""" Calculates the gain from splitting data with the specified 
		attribute """

		return 0


class Node:
	""" A single node representation in a decision tree """

	def __init__(self, attribute):
		""" Initializes new node with attribute to split on """
		self.attribute = attribute
		self.children = []

	def __str__(self):
		""" Returns a string representing the node """
		str = 'Node splitting on ' + self.attribute
		return str


	#def generate_tree(self, data, attributes, target_attr):


	#def choose_attr(self, data, attributes):
	#	""" Returns the best attribute to split on next """

	










	def get_values(self, attr, subsetIndices = None):
		""" Returns attribute type and a list of values under specified attribute 
		for a specified subset of data points """
		
		# use whole set if no subset specified
		if subsetIndices is None:
			subsetIndices = range(self.numData)

		# get attribute index
		attrIndex = self.attributes.index(attr)

		# get attribute type
		attrType = self.attrTypes[attrIndex]

		# get values but ingnore missing ones
		values = []
		for index in subsetIndices:
			val = self.data[index][attrIndex]
			if val != '?':
				values.append(val)

		return attrType, values


def entropy(data, subsetIndices = None):
	""" Calculates entropy of data points in given dataSet specified 
	by subset indices """

	distribution = {}

	attrType, values = dataSet.get_values(dataSet.classAttr, subsetIndices)
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


def split(dataSet, attr, subsetIndices = None):


def gain(dataSet, attr, subsetIndices = None):
	""" Calculates the gain from splitting the specified subset with
	the specified attribute """

	#attrType, values = self.get_values(attr, subsetIndices)
	
	if attrType == dataSet.NUMERIC:
		groups = dataSet.splitNumeric(attr, subsetIndices)
	else:
		groups = dataSet.split(attr)

	return 0



