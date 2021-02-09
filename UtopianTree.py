#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):

    return 2 ** ((n+3)//2) + ((-1)**n - 3) // 2

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        print(utopianTree(n))
