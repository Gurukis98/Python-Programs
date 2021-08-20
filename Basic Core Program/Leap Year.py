"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 5:45 PM
*Title  : Find Leap Year or Not
"""

year = int(input("Please Enter a Year:"))

try:
    if 999 > year:
        raise ValueError("Invalid Input")

    elif 9999 <= year:
        raise ValueError("Invalid Input")

    else:
        if year % 100 != 0:
            print(year, "is Leap Year")
        else:
            print(year, "is Not a Leap Year")

except ValueError as e:
    print(e)
