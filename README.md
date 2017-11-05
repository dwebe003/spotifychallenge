### Project:	
	Spotify Puzzle -- Cat vs. Dog

### Contents:   
	This program accepts a number of testcases, at most 100, and then prompts
	the user to enter a number of cats, dogs, and viewers (c, d, v) where 
	1 <= c, d <= 100  and  0 <= v <= 500. Once these conditions have been set,
	the user enters in a "vote" consisting of 2 identifiers. The first identifier
	is the pet this voter wants to stay, and the second identifier is the pet
	this voter wants to leave. Each identifier begins with the letter 'C' or 'D' 
	(lowercase also accepted) and ends with a number specifying which cat or dog 
	to vote for. The program then runs through an algorithm to determine the
	maximum number of voters satisfied.

### Algorithm:	
	The algorithm I used to calculate maximum voters satisfied is as follows:

	1) If we are voting for a Cat (or Dog), add the vote to the left (or right) 
					partition of the Graph.

	2) Next we check for edge contradiction. Votes are in the format (a, b). 
		So if we add a new vote (a, b) and check each vote (c, d) in the opposite
		partition, and we find that a=d or b=c then we cannot augment our
		number of satisfied voters.

	note) This problem is equivalent to finding the max cardinality of each subcover
			of a bipartite graph. Cats on the left, dogs on the right.


//----------------------------------------------------------------//

	TO RUN THIS PROGRAM:
		1) Open Terminal/Command Prompt
		2) Navigate to folder containing catvsdog.py (using cd commands)
		3) Type what is contained in these quotations: "python catvsdog.py"
		
### File:       
	catvsdog.py
### Author:     
	David Weber
### Date:       
	11/03/2017
### Version:    
	1.0


 


