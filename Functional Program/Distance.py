"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 3:20 PM
*Title  :Distance Between Two Lines
"""
import math

class Distance:
    flag = True

    while flag == True:
        try:
            X = int(input("Enter a Value of X:"))
            Y = int(input("Enter a Value of Y:"))
            if (X and Y) == 0:
                raise ValueError()
                flag = False
            else:
                num = (X * Y) + (Y * Y)
                distance = math.sqrt(num)
                print("Distance Of point from the origin:", distance)
                flag = False

        except ValueError:
            print('Invalid Input')