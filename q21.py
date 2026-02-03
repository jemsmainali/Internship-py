# Write a program to find product of two matrices.

#Answer1
A=[[1,2],
   [3,4]]
B=[[5,6],
   [7,8]]
result=[[0,0],
               [0,0]]

for i in range (len(A)):
    for j in range (len(B[0])):
        for k in range (len(B)):
            result[i][j] = result[i][j] + A[i][k] * B[k][j]

print("Sum of matrix is: ")
for row in result:
    print(row)


#Answer2
def product_of_matrix(A,B):
    result1 = [[0,0,0],
              [0,0,0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result1[i][j] = result1[i][j] + A[i][k] * B[k][j]
    return result1

A=[[1,2,4],
   [3,4,6]]
B=[[5,6,1],
   [7,8,2]]
prod_matrix = product_of_matrix(A,B)
for row in prod_matrix:
    print(row)