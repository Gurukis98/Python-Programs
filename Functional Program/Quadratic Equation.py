"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 2:45 PM
*Title  :Find Quadratic Equation of Root1 and Root2
"""

import cmath
a = int(input("Enter The Value of a:"))
b = int(input("Enter The Value of b:"))
c = int(input("Enter The Value of c:"))

delta = (b * b) - (4 * a * c)
Root1 = (- b + cmath.sqrt(delta)) / (2 * a)
Root2 = (- b - cmath.sqrt(delta)) / (2 * a)
print("Quadratic Equation For Root1:", Root1)
print("Quadratic Equation For Root2:", Root2)

