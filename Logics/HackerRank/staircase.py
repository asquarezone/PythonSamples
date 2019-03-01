#!/bin/python3
#https://www.hackerrank.com/challenges/staircase/problem
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for index in range(n):
        spaces = n-index
        for space in range(spaces-1):
            print(' ',end='')
        for hash in range(n-spaces+1):
            print('#',end='')
        print('',end='\n')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
