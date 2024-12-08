file = open("day4/input.txt",'r')

matrix = []

for line in file:
    matrix.append(line)

xmas = ['X','M','A','S']
xmasStr = "XMAS"

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        tab = []
        if xmasStr in matrix[i] or xmasStr[::-1] in matrix[i]: #W PRAWO O LEWO             
            print("Tak nie wyjdzie xd")