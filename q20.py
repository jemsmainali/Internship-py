# Write a program to find sum of two matrices.

#Answer1
A=[[1,5,8],
   [3,4,9]]
B=[[4,6,2],
   [5,7,8]]
sum_of_matrix=[[0,0,0],
               [0,0,0]]

for i in range (len(A)):
    for j in range (len(A[0])):
        sum_of_matrix[i][j] = A[i][j] + B[i][j]

print("Sum of matrix is: ")
for row in sum_of_matrix:
    print(row)


#Answer2
def matrix_addition(A,B):
    result=[[0,0,0],
            [0,0,0],
            [0,0,0],]

    for i in range (len(A)):
        for j in range (len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

A=[[1,5,8],
   [3,4,9],
   [2,4,5]]
B=[[4,6,2],
   [5,7,8],
   [1,2,3]]
sum_matrix =matrix_addition(A,B)

print("the sum of matrix is: ")
for row in sum_matrix:
    print(row)

















