"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 6:40 PM
*Title  : Flip coin simulation at given range and their percentage
"""
import random

Heads = 'Heads'
Tails = 'Tails'
noOfHead = 0
noOfTails = 0

def flipCoin():
    randomCheck = random.uniform(0, 1)
    return Heads if randomCheck < 0.5 else Tails

try:
    Num = int(input("Enter Number of Flips:"))
    if Num <= 0:
        raise ValueError("Invalid Input")
    else:
        for i in range(0, Num):
            outPut = flipCoin()
            if outPut == 'Heads':
                noOfHead += 1
            else:
                noOfTails += 1
            print(flipCoin())

except ValueError as e:
    print(e)

try:
    if (noOfTails and noOfHead) == 0:
        raise ZeroDivisionError("Enter another number")
    else:
        percentageOfHeads = noOfHead * 100 / Num
        percentageOfTails = noOfTails * 100 / Num
        print("Total number of Heads:: ", +noOfHead)
        print("Total number of Tails:: ", +noOfTails)
        print("Percentage of Heads:: ", +percentageOfHeads)
        print("Percentage of Tails:: ", +percentageOfTails)

except ZeroDivisionError as e:
    print(e)