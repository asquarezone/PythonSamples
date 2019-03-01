#!/bin/python3
# https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys
import decimal

# Complete the plusMinus function below.
def plusMinus(arr):
    decimal.getcontext().prec = 6
    total = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for item in arr:
        if item > 0:
            positive = positive+1
        elif item < 0:
            negative = negative+1
        else:
            zero = zero + 1
    positive = decimal.Decimal(positive)/decimal.Decimal(total)
    print(positive)
    negative = decimal.Decimal(negative)/decimal.Decimal(total)
    print(negative)
    zero = decimal.Decimal(zero)/decimal.Decimal(total)
    print(zero)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
