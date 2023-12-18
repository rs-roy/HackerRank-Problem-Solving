#!/bin/python3

import math
import os
import random
import re
import sys

def solve(a):
    
    capitalized_name = ""

    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            capitalized_name = capitalized_name + s[i].upper()
        elif s[i].isalpha() and s[i-1] == " ":
            capitalized_name = capitalized_name + s[i].upper()
        else:
            capitalized_name = capitalized_name + s[i]

    return capitalized_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
