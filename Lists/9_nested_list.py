from time import process_time

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
''' iterating through element '''
for row in matrix:
    for i in row:
        print(i,end=" ")
    print()

""" iterating through index """
print()
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(mat)):
    # print(mat[i])
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()

good = []
mood = [0,0,0]
for _ in range(3):
    good.append(mood[:])
print(good)
good[0][0] = 1
print(good)