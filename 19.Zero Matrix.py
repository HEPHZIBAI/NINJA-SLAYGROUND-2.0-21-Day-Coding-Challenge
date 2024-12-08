'''
Problem statement
You are given a matrix 'MATRIX' of dimension 'N' x 'M'. Your task is to make all the elements of row 'i' and column 'j' equal to 0 if any element in the ith row or jth column of the matrix is 0.

Note:

1) The number of rows should be at least 1.

2) The number of columns should be at least 1.

3) For example, refer to the below matrix illustration: 

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= N <= 100
1 <= M <= 100
-10^9 <= MATRIX[i][j] <= 10^9

Where 'MATRIX[i][j]' denotes the matrix element.
Follow Up:

Can you solve it with the space complexity of O(1)?

Time limit: 1 sec


Sample Input 1:
2 3
2 4 3
1 0 0
Sample Output 1:
2 0 0 
0 0 0 
Sample Input 2:
1 1 
5
Sample Output 2:
5 


Hints:
1. Think about how to identify the rows and columns containing a '0' element and then modify the matrix accordingly to make all elements in those rows and columns equal to 0.
2. You can use the first row and first column of the matrix itself as indicators to mark whether a particular row or column needs to be zeroed
'''

from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(m))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(n))
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_has_zero:
        for j in range(m):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(n):
            matrix[i][0] = 0

    return matrix