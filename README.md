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
	to vote for. 

### Algorithm:
	The algorithm I used to calculate maximum voters satisfied is as follows:

	1) If we are voting for a Cat, add 1 to the corresponding cat number in cats list
		and subtract 1 from the corresponding dog number in dogs list. 

	2) So long as the specified Cat is scoring positively, AND the specified Dog is 
		scoring negatively (or zero), this cat person is satisfied. So add 1 
		to satisfied.

	3) Do the above, conversely, if voting FOR dog and AGAINST cat.


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


 


