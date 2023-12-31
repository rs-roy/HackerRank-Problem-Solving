#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    date_obj1 = datetime.strptime(t1, date_format)
    date_obj2 = datetime.strptime(t2, date_format)
    delta = abs((date_obj1 - date_obj2)).total_seconds()
    
    return str(delta)[:-2]    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
