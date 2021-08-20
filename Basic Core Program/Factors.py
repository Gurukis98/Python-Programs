"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 6:10 PM
*Title  : Factors Using Integers
"""
try:
    Num = int(input("Enter Any Number:"))
    if Num <= 0:
        raise ValueError
    else:
        i = 2
        print("The Factors of", Num, "are:")
        while(Num != 0):
            reminder = Num % i
            if( reminder == 0 ):
                Num = Num / i
                print(i)
            else:
                i = i+1

except ValueError:
    print("The Number", Num, "is Invalid")
