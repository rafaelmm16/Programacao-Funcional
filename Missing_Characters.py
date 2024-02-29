#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Create a set containing all lowercase letters and digits
    all_chars = set("abcdefghijklmnopqrstuvwxyz0123456789")
    
    # Remove characters from the set if they exist in the input string
    for char in s:
        if char in all_chars:
            all_chars.remove(char)
    
    # Convert the remaining set elements to a sorted list
    missing_chars = sorted(all_chars)
    
    # Join the sorted list elements into a single string and return it
    return ''.join(missing_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
