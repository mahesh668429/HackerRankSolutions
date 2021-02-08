#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # 10 20 40 50 100
    # 5 25 50 120
    result=[]
    ranked=sorted(list(set(ranked)))
    n=len(ranked)
    global x
    x=0
    for i in player:
        print(x)
        while x < n and ranked[x] <= i:
            x+=1
        result.append(n-x+1)
    return result

if __name__ == '__main__':
    ranked = list(map(int, input().rstrip().split()))
    player = list(map(int, input().rstrip().split()))

    print(climbingLeaderboard(ranked, player))