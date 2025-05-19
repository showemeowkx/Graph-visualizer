import random

def defineValue(k):
    definer = random.uniform(0, 2)
    definerMulti = float(definer) * k
    if definerMulti < 1:
        return 0
    else: 
        return 1

def fillMatrix(n1, n2, n3, n4, formula):
    size = n3 + 10
    matrix = [[0]*size for _ in range(size)]
    k = eval(formula)
    seedVariant = str(n1) + str(n2) + str(n3) + str(n4)
    random.seed(int(seedVariant))

    for i in range(size):
        for j in range(size):
            matrix[i][j] = defineValue(k)

    return matrix

def convertMatrix(matrix):
    size = len(matrix)
    matrixUndir = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                matrixUndir[i][j] = 1
                matrixUndir[j][i] = 1

    return matrixUndir

def stringify(matrix, paddings):
    string = ""
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            string += str(matrix[i][j]) + (" " * paddings)
        string += "\n"

    return string

def getEdgeList(matrix):
    edges = []
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                edges.append((i, j))
    
    return edges

def getParallelEdges(edges):
    parallelEdges = []
    for i, j in edges:
        if i != j and (j, i) in edges:
            if (i, j) not in parallelEdges:
                parallelEdges.append((i, j))
          
    return parallelEdges

def multiplyMatrices(A, B):
    size = len(A)
    multipliedMatrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                multipliedMatrix[i][j] += A[i][k] * B[k][j]

    return multipliedMatrix

def raiseMatrix(matrix, power):
    raisedMatrix = [row[:] for row in matrix]
    for _ in range(power-1):
        raisedMatrix = multiplyMatrices(raisedMatrix, matrix)

    return raisedMatrix

def transposeMatrix(matrix):
    size = len(matrix)
    transposed = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            transposed[j][i] = matrix[i][j]
    
    return transposed