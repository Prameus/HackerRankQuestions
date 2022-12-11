#!/bin/python3

import math
import os
import random
import re
import sys



def fizzBuzz(n):
    for i in range(1,n):
            if i%3 == 0:
                print('Fizz')
            elif i%5 == 0:
                print('Buzz')
            elif i%15 == 0:
                print('FizzBuzz')
            else:
                print(i)

fizzBuzz(100)
