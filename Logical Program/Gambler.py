"""
*Author : Guruprasanth
*Date   : 20-08-2021
*Time   : 6:30 AM
*Title  :Gambler Program To Find Win And Loss Percentage
"""

import random

class Gambler:

    Won = 0
    Lose = 0
    initialAmount = int(input("Enter Your Amount:"))
    goal = int(input("Enter goal:"))
    flag = True
    Random = 0
    goalCheck = initialAmount

    while flag:
        betAmount = int(input("Enter Your Betting Amount:"))
        randomCheck = random.uniform(0, 1)
        basicAmount = initialAmount - betAmount
        Random += 1
        if initialAmount < 0:
            flag = False
            break
        elif initialAmount == goal:
            break
        elif basicAmount < 0:
            print("Amount is Not Enough")
            print("Amount Available: ", initialAmount)
            break
        elif goal < goalCheck:
            print("Invalid Goal")
        elif randomCheck < 0.5:
            print("Lose")
            basicAmount = initialAmount - betAmount
            Lose += 1
        else:
            print("Won")
            basicAmount = initialAmount + betAmount
            Won += 1

    wonPercentage = (Won * 100) / Random
    losePercentage = (Lose * 100) / Random
    print("At End Of The  Game Total Amount:", initialAmount)
    print("Won Percentage:", wonPercentage)
    print("Lose Percentage:", losePercentage)

gambler = Gambler()
