"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 3:30 PM
*Title  :Sum of the Three Integer is Zero
"""

def findTriplets(arr, n):
    Array = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    Array = True

    if Array == False :
        print("Array Not Exist ")


arr = [0, -1, 2, -3, 1, -5, 3, -9]
n = len(arr)
findTriplets(arr, n)
