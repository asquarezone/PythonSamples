#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum_primary_diagonal = 0
    sum_secondary_diagonal = 0
    secondary_diagonal_j=len(arr)-1
    secondary_diagonal_i = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                #primary_diagnol
                sum_primary_diagonal = sum_primary_diagonal+arr[i][j]
            if i ==secondary_diagonal_i and j ==secondary_diagonal_j:
                sum_secondary_diagonal = sum_secondary_diagonal + arr[i][j]
        secondary_diagonal_i = secondary_diagonal_i+1
        secondary_diagonal_j = secondary_diagonal_j-1

    return abs(sum_primary_diagonal-sum_secondary_diagonal)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
