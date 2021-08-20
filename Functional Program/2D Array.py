"""
*Author : Guruprasanth
*Date   : 18-08-2021
*Time   : 4:30 PM
*Title  :2D array
"""

class TwoDimentionalArray:

    i=0
    matrix = []
    arr = []
    flag = True

    while flag == True:
        try:
            Row = int(input("Please Enter Number of Rows:"))
            Column = int(input("Please Enter Number of Columns:"))
            if (Row and Column) == 0:
                flag = False
                raise ValueError()
            else:
                for i in range(Row):
                    for j in range(Column):
                        print("Enter value for", j, "Column &", i, "Row:")
                        Num = int(input())
                        arr.append(Num)
                    matrix.append(arr)
            flag = False

        except ValueError:
            print('Invalid Input')

    print(arr)