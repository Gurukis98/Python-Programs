"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 5:30 PM
*Title  : Find Leap Year or Not Using Power of 2
"""
import math
import random


def CheckLeap(Year):
    if (Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0):
        print("Given Year is a leap Year")
    else:
        print("Given Year is not a leap Year")


N = random.randint(0, 32)
print("N:", N)
Year = int(math.pow(2, N))
CheckLeap(Year)
