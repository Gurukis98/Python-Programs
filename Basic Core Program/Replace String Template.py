"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 5:43 PM
*Title  : Replace String template
"""

try:
    name = input("Enter Your Name:")
    nameLength = len(name)

    if nameLength >= 3:
        print("Hello ", name, ",How are you?")
    else:
       raise NameError()

except NameError:
        print("Invalid Input")


