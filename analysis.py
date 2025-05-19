from matrix import getEdgeList, raiseMatrix

# matrixDir = fillMatrix(9, 7, 0, 2, '1.0 - n3*0.005 - n4*0.005 - 0.27')

def calcSemiDegrees(matrix):
    size = len(matrix)
    degreesDict = {'in': [0]*size, 'out': [0]*size}
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                degreesDict['out'][i]+=1
                degreesDict['in'][j]+=1
                
    return degreesDict

def calcDegrees(matrix, mode):
    size = len(matrix)
    degrees = [0]*size
    edges = getEdgeList(matrix)
    usedEdges = []
    for (i, j) in edges:
        if mode == 0:
            if (i, j) not in usedEdges and (j, i) not in usedEdges:
                usedEdges.append((i, j))
                degrees[i]+=1
                degrees[j]+=1
        else:
            if (i, j) not in usedEdges:
                usedEdges.append((i, j))
                degrees[i]+=1
                degrees[j]+=1

    return degrees

def isRegular(degrees):
    if all(i == degrees[0] for i in degrees):
        return degrees[0]
    
    return False

def getIsolated(degrees):
    size = len(degrees)
    isolatedVertices = []
    for i in range(size):
        if degrees[i] == 0:
            isolatedVertices.append(i+1)

    return isolatedVertices

def getReachable(semiDegrees):
    size = len(semiDegrees['in'])
    reachableVertices = []
    for i in range(size):
        if semiDegrees['in'][i] > 0 :
            reachableVertices.append(i+1)

    return reachableVertices

def getLeaves(degrees):
    size = len(degrees)
    leaves = []
    for i in range(size):
        if degrees[i] == 1:
            leaves.append(i+1)

    return leaves

def getPathsEdgeVertices(matrix, length):
    size = len(matrix)
    edgeVertices = []
    raisedMatrix = raiseMatrix(matrix, length)
    for i in range(size):
        for j in range(size):
            if raisedMatrix[i][j] > 0:
                edgeVertices.append((i+1, j+1))

    return edgeVertices

def getDoublePathsIntermidiateVertices(matrix):
    size = len(matrix)
    paths = []
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    paths.append([i+1, k+1, j+1])

    return paths

def getTripplePathsIntermidiateVertices(matrix):
    size = len(matrix)
    paths = []
    for i in range(size):
        for k in range(size):
            if matrix[i][k] == 1:
                for l in range(size):
                    if matrix[k][l] == 1:
                        for j in range(size):
                            if matrix[l][j] == 1:
                                paths.append([i+1, k+1, l+1, j+1])

    return paths

def buildPathsDict(matrix, length):
    pathsDict = {}
    edgeVertices = getPathsEdgeVertices(matrix, length)

    if length == 2:
        intermidiateVertices = getDoublePathsIntermidiateVertices(matrix)
    elif length == 3:
        intermidiateVertices = getTripplePathsIntermidiateVertices(matrix)
    else: raise Exception('Only lengths of 2 and 3 are supported.')

    for i, j in edgeVertices:
        for vert in intermidiateVertices:
            if i == vert[0] and j == vert[length]:
                key = f"({i}) -> ({j})"
                if key in pathsDict:
                    pathsDict[key].append(vert)
                else:
                    pathsDict[key] = [vert]
    
    return pathsDict

def buildReachabilityMatrix(matrix):
    size = len(matrix)
    reachabilityMatrix = [row[:] for row in matrix]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if reachabilityMatrix[i][k] == 1 and reachabilityMatrix[k][j] == 1:
                    reachabilityMatrix[i][j] = 1

    return reachabilityMatrix

def buildStrongConnectivityMatrix(reachabilityMatrix):
    size = len(reachabilityMatrix)
    strongConnectivityMatrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if reachabilityMatrix[i][j] == 1 and reachabilityMatrix[j][i] == 1:
                strongConnectivityMatrix[i][j] = 1

    return strongConnectivityMatrix

def getStrongComponents(matrix):
    size = len(matrix)
    reachabilityMatrix = buildReachabilityMatrix(matrix)
    strongConnectivityMatrix = buildStrongConnectivityMatrix(reachabilityMatrix)

    visited = [False] * size
    components = []

    for i in range(size):
        if not visited[i]:
            component = []
            for j in range(size):
                if strongConnectivityMatrix[i][j] and not visited[j]:
                    component.append(j+1)
                    visited[j] = True
                else:
                    components.append([j+1])
                    visited[j] = True
            if component:
                components.append(component)

    return components

def getComponentsDict(components):
    componentsDict = {}
    for compIndex, comp in enumerate(components):
        for vert in comp:
            componentsDict[vert] = compIndex+1

    return componentsDict

def buildCondensationMatrix(matrix):
    components = getStrongComponents(matrix)
    componentsDict = getComponentsDict(components)
    sizeM = len(matrix)
    sizeC = len(components)

    condensationMatrix = [[0]*sizeC for _ in range(sizeC)]

    for i in range(sizeM):
        for j in range(sizeM):
            if matrix[i][j] == 1:
                ci = componentsDict[i+1]
                cj = componentsDict[j+1]
                if ci != cj:
                    condensationMatrix[ci-1][cj-1] = 1
    
    return condensationMatrix