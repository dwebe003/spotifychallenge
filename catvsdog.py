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
#				1) If we are voting for a Cat, add 1 to the corresponding cat number in cats list
#						and subtract 1 from the corresponding dog number in dogs list. 
#
#				2) So long as the specified Cat is scoring positively, AND the specified Dog is 
#						scoring negatively (or zero), this cat person is satisfied. So add 1 
#						to satisfied.
#
#				3) Do the above, conversely, if voting FOR dog and AGAINST cat.
#
#########################################################################################
#########################################################################################

def voter(c, d, v):

	# initialize cats and dogs arrays of size c and d, respectively, and set entries to 0.
	# these will store the voting scores for each cat and dog.
	cats = [0] * c
	dogs = [0] * d
	satisfied = 0
	
	# iterates below process for each voter
	for i in range(v):
		# asks for voting input
		print("Cast your vote! (e.g. C1 D1)")
		arr = raw_input().split()
		string1 = arr[0]
		string2 = arr[1]
		
		# checks same species has not been entered, e.g. C1 C2 or D1 D1
		if(string1[0] == string2[0]):
			print("Error: You can't backstab the same species you voted for!")
			i -= 1
			continue
		
		# checks if voter is cat person
		elif(string1[0] == 'C' or string1[0] == 'c'):
			# determines which cat and dog we are going to work with
			x = int(string1[1])
			y = int(string2[1])
			
			# increments score of specified cat
			cats[x-1] += 1
			# decrements score of specified dog
			dogs[y-1] -= 1
			
			# if specified cat is scoring positively && specified dog is not positive,
			# increment satisfied
			if(cats[x-1] > 0 and dogs[y-1] <= 0):
				satisfied += 1
				
		# checks if voter is dog person	
		elif(string1[0] == 'D' or string1[0] == 'd'):
			# determines which cat and dog we are going to work with
			x = int(string1[1])
			y = int(string2[1])
			
			# increments score of specified dog
			dogs[x-1] += 1
			# decrements score of specified cat
			cats[y-1] -= 1
			
			# if specified dog is scoring positively && specified cat is not positive,
			# increment satisfied
			if(dogs[x-1] > 0 and cats[y-1] <= 0):
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

