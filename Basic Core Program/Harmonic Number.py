"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 5:30 PM
*Title  : Harmonic Number
"""

try:
    n = int(input("Enter a nth Harmonic Value:"))

    if n > 0:
        for i in range(1, n+1):
            print("Harmonic Number:""1/",i)
    else:
        raise ValueError("Invalid Input")

except ValueError as e:
    print(e)
