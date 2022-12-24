# Program to add two matrices using nested loop
X = [[1,2,3],
[4 ,5,6],
[7 ,8,9]]
Y = [[9,8,7],
[6,5,4],
[3,2,1]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]
# iterate through rows
for i in range(len(X)):
    for j in range(len(Y)):
# iterate through columnsfor j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
        print(r)
# program for Subtraction of Two Matrices-
matrix1 = [[10, 11, 12],
[13, 14, 15],
[16, 17, 18]]
matrix2 = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
rmatrix = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] - matrix2[i][j]
for r in rmatrix:
    print(r)
# program for Multiply Two 3*3 Matrices entered by User
matOne = []
print("Enter 9 Elements for First Matrix: ")
for i in range(3):
    matOne.append([])
for j in range(3):
    num = int(input())
matOne[i].append(num)
matTwo = []
print("Enter 9 Elements for Second Matrix: ")
for i in range(3):
        matTwo.append([])
        for j in range(3):
            num = int(input())
matTwo[i].append(num)
matThree = []
for i in range(3):
    matThree.append([])
for j in range(3):
    sum = 0
for k in range(3):
    sum = sum + (matOne[i][k] * matTwo[k][j])
matThree[i].append(sum)
print("\nMultiplication Result of Two Given Matrix is:")
for i in range(3):
    for j in range(3):
	print()
# Program to transpose a matrix using a nested loop
