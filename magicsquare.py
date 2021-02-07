#!/bin/python3

import os
from itertools import *


# Complete the formingMagicSquare function below.
def formingmagicsquare(s):
    ans = 81
    for P in permutations(range(1, 10)):
        '''permutations fun return all permutation of the elements in a given iterable '''
        if sum(P[0:3]) == sum(P[3:6]) == sum(P[0::3]) == sum(P[1::3]) == (P[0] + P[4] + P[8]) == (
                P[2] + P[4] + P[6]) == 15:
            '''[x:y] means get the elements from x to y index excluding y
               [x::y] means get the the elements from x to end of the list with an interval of y '''
            ans = min(ans, sum(abs(P[i] - s[i]) for i in range(0, 9)))
    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []

    for _ in range(3):
        s.extend(list(map(int, input().rstrip().split())))

    result = formingmagicsquare(s)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
