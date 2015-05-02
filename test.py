import sys, getopt
from DataSet import *

def main(argv = None):
	if argv is None:
		argv = sys.argv

	if len(argv) < 3:
		print 'Please specify a training set and its metadata file.'
		return 1

	dt = DataSet(argv[1], argv[2])
	#print dt.attributes
	#print dt.get_subset([1,2]).get_values('winner')
	print 'entropy: ' + str(dt.get_subset().entropy())
	#print dt.data['winner']

	#print dt.entropy()
	#print dt.unclassified

	#print sys.getsizeof(dt.data['winner']['dataPoints'])
	#print dt.data['winner']['dataPoints']

	return 0


if __name__ == '__main__':
	sys.exit(main())
