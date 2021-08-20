"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 4 PM
*Title  :Find the Value of Wind Chill
"""
import math
import random

t = random.uniform(50, 212)
print("Temperature:", t)
v = random.uniform(0, 4)
print("Speed:", v)
V = math.pow(v, 0.16)
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * V
print("Wind Chill:", w)
