class Mammals:
    def __init__(self):
	    ''' Constructor for thsi class.'''
		# Create some member annimals
		self.members = ['Tiger', 'Elephant', 'Wild']
		
	def printMembers(self):
	    print('printing members of the mammals class)
		for member in self.members:
		    print('\t%s' % member)