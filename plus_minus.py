
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    pos: int = 0
    neg: int = 0
    zero: int = 0

    length = len(arr)

    for i in arr:
        if (i < 0):
            neg += 1
        elif (i == 0):
            zero += 1
        elif (i > 0):
            pos += 1

    print("{:.6f}".format(pos/length))
    print("{:.6f}".format(neg/length))
    print("{:.6f}".format(zero/length))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
