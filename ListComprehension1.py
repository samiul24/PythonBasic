matrix = []

for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

matrix1 = [ [j for j in range(5)] for i in range(5)]
print(matrix1)

matrix2 = [ [j] for i in range(5) for j in range(5)]
print(matrix2)
