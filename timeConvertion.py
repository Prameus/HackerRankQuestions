#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):

    numbers = ""
    texts = ""

    for i in s:
        if i == "A" or i == "P":
            texts += i
            print("texts:",texts)
            break
        else:
            numbers += i
            print("number:", numbers)

    x = numbers.split(":")
    print(x)

    if texts == "P":
        if x[0]=="12":
            if (int(x[0]) > 24):
                x[0] = (int(x[0]) - 24)
            elif (int(x[0]) < 10):
                x[0] = x[0]
            solution = ":".join(x)
            print(solution)
            return solution
        else:
            x[0] = str(int(x[0]) + 12)
            if (int(x[0]) > 24):
                x[0] = (int(x[0]) - 24)
            elif (int(x[0]) < 10):
                x[0] = x[0]
            solution = ":".join(x)
            print(solution)
            return solution
    
    elif texts == "A":
        if (int(x[0]) < 12):
            print(s)
            return s
        else:
            x[0] = str(int(x[0]) - 12)
            x[0] = "0" + x[0]
            solution = ":".join(x)
            print(solution)
            return solution
            

timeConversion("12:45:54PM")
