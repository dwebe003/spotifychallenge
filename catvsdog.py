#########################################################################################
#
#   File:       catvsdog.py
#   Author:     David Weber
#   Date:       11/03/2017
#   Version:    1.0
#
#	Project:	Spotify Puzzle -- Cat vs. Dog
#
#
#   Contents:   This program accepts a number of testcases, at most 100, and then prompts
#				the user to enter a number of cats, dogs, and viewers (c, d, v) where 
#				1 <= c, d <= 100  and  0 <= v <= 500. Once these conditions have been set,
#				the user enters in a "vote" consisting of 2 identifiers. The first identifier
#				is the pet this voter wants to stay, and the second identifier is the pet
#				this voter wants to leave. Each identifier begins with the letter 'C' or 'D' 
#				(lowercase also accepted) and ends with a number specifying which cat or dog 
#				to vote for. 
#
#	Algorithm:	The algorithm I used to calculate maximum voters satisfied is as follows:
#
#				1) If we are voting for a Cat (or Dog), add the vote to the left (or right) 
#					partition of the Graph.
#
#				2) Next we check for edge contradiction. Votes are in the format (a, b). 
#					So if we add a new vote (a, b) and check each vote (c, d) in the opposite
#					partition, and we find that a=d or b=c then we cannot augment our
#					number of satisfied voters.
#
#				note) This problem is equivalent to finding the max cardinality of each subcover
#						of a bipartite graph. Cats on the left, dogs on the right.
#
#########################################################################################
class BiGraph:
	def __init__(self):
		self.left = []
		self.right = []
		self.edges = []
		
	def addleft(self, vote):
		self.left.append(vote)
	
	def addright(self, vote):
		self.right.append(vote)
#########################################################################################

def voter(c, d, v):

	# initialize cats and dogs arrays of size c and d, respectively, and set entries to 0.
	# these will store the voting scores for each cat and dog.
	G = BiGraph()
	catVotes = []
	dogVotes = []
	satisfied = 0
	
	# iterates below process for each voter
	for i in range(v):
		# asks for voting input
		print("Cast your vote! (e.g. C1 D1)")
		arr = raw_input().split()
		string1 = arr[0]
		string2 = arr[1]

		vote = (string1, string2)
		
		# checks same species has not been entered, e.g. C1 C2 or D1 D1
		if(string1[0] == string2[0]):
			print("Error: You can't backstab the same species you voted for!")
			i -= 1
			continue
		
		# checks if voter is cat person
		elif(string1[0] == 'C' or string1[0] == 'c'):
			G.addleft(vote)
			catVotes.append(vote)
			contradiction = 'false'
			
			if len(dogVotes) == 0:
				satisfied += 1
			else:
				# checks for contradiction
				for x in range(len(dogVotes)):
					if( (vote[0][1] == G.right[x][1][1]) or (vote[1][1] == G.right[x][0][1]) ):
						contradiction = 'true'
						break
					else:
						satisfied += 1
						
				# if no contradictions found, increment our max subcover
				if contradiction == 'false':
					satisfied += 1
			
				
		# checks if voter is dog person	
		elif(string1[0] == 'D' or string1[0] == 'd'):
			G.addright(vote)
			dogVotes.append(vote)
			contradiction = 0
			
			if len(catVotes) == 0:
				satisfied += 1
			else:
				# checks for contradiction
				for x in range(len(catVotes)):
					if( (vote[0][1] == G.left[x][1][1]) or (vote[1][1] == G.left[x][0][1]) ):
						contradiction = 'true'
						break
					else:
						contradiction = 'false'
						
				# if no contradictions found, increment our max subcover
				if contradiction == 'false':
					satisfied += 1
			
		else:
			print("Error: recast please...\n")
			i -=1
			continue
			
	return satisfied
		


#########################################################################################

def votingProcess(numTests):
	# initializes cats, dogs, viewers to 0
	c, d, v = 0, 0, 0
	
	# for each test case we receive our c, d, v inputs and then call our voter eval function
	for i in range(numTests):
		print("\nPlease enter the number of cats, dogs, and voters, separated by a space: ")
		arr = raw_input().split()
		c = int(arr[0])
		d = int(arr[1])
		v = int(arr[2])
		
		maxSatisfied = voter(c, d, v)
		print '\nMax number of voters satisfied: ', maxSatisfied, '\n\n'

#########################################################################################

def intro():
	numTests = input('\nPlease enter how many tests you would like to try: ')
	
	if numTests > 0 and numTests <=100:
		return numTests
	else:
		print("No tests requested. Exiting...")
		quit(1)

#########################################################################################

def main():

	
	numTests = intro()

	x = votingProcess(numTests)


if __name__ == '__main__':
	main()

