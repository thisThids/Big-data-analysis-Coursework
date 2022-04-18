#! /usr/bin/env python3
import sys

#input comes from STDIN (standard input)
line = sys.stdin
next(line)
for word in line:
    if not line:
        break
   # To split each line

    words = word.split(',')
    
    for i in words[8]:
        if '-' in i:
            
        # After inspect temperature values found that it contain '-' values
        # It needed to be converted to integer for further statistical calculation purposes
            Replacement = i.replace('-', '0')
 
        # changes are made in the list
            words[8] = Replacement
    
    # Print words that are needed and append "1" at the end for counting purpose in reducer 
    print(words[1],words[8], "1")
   



