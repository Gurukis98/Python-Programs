"""
*Author : Guruprasanth
*Date   : 20-08-2021
*Time   : 3 PM
*Title  : Randomly Generating Coupon Numbers
"""

import random

class Coupon:
    @staticmethod
    def randomCoupon():
        i=0
        couponList = []
        N = int(input("Enter The Coupon Number:"))

        while N >= (i+1):
            randomNumber = random.randint(1,100)

            if (not (couponList.__contains__(randomNumber))):
                couponList.append(randomNumber)
                i += 1
            elif N:
                flag = False
            else:
                print("no contain")
            print(couponList)

coupon = Coupon()
coupon.randomCoupon()