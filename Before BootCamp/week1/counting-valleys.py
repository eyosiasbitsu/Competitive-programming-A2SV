import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    output = 0
    count = 0
    for char in path:
        if char == 'U':
            output += 1
            if output == 0:
                count += 1
        else:
            output -= 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')