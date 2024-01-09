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

    if s[:2] == "12":
        if s[-2:] == "AM":
            return f"00{s[2:-2]}"
        if s[-2:] == "PM":
            return f"12{s[2:-2]}"

    if s[-2:] == "AM":
        return f"{format(int(s[:2]), '02')}{s[2:-2]}"
    if s[-2:] == "PM":
        return f"{int(s[:2])+12}{s[2:-2]}"

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')
