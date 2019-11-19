#Ryan Moses
#CSCI - Section A
#Week - Part A

#PrintOutput
Method was to copy function from lab 10B

#LoadFile
I opened the file and used a for loop for each line in the text file, 
stripped the newline command from each line, 
then appended each stripped line into a list, 
and returned list

#UpdateString
used a 2 for loops nested within eachother to append each character of base string into a list seperately,
changed the character in chosen index point to chosen string,
joined the list into string

#FindWordCount
used for loop to check each part of list,
checked if lowercase version of index was the same as lowercase version of target string,
each time if statement was true 1 was added to counter variable(set to 0 at start)

#ScoreFinder
used for loop with range of length of players list,
checked if lowercase version of name from list was the same as lowercase version of target name,
if the if statement was true the index number (i) was used to index both player list and score list,
x was used so that if player name was not found in list the 'player not found' output was given

#Union
output list was initialized,
for loop used to loop through first list,
checked if each part of list (i) was already in the output list,
if i was not already in output then append i into output list,
repeated same method with list 2

#Intersection
output list was initialized,
for loop used to loop through first list (similar to Union),
for each iteration of for loop the value i was checked to see if it was also in list 2,
if i was in list 2 then append i to output list,
(since i is always a member or list 1, list 1 did not need to be checked, only list 2)

#NotIn
output list was initialized,
for loop used to loop through first list (similar to Union and Intersection),
for each iteration of for loop the value i was checked to see if it was in list 2,
if i was not in list 2 then it was appended to output list,
(same code setup as Intersection, just added 'not' to if statement to reverse the outcome)