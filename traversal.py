from analysis import getReachable, calcSemiDegrees, buildTraversalTreeMatrix

def findStartVertex(matrix):
    size = len(matrix)
    for v in range(size):
        if sum(matrix[v]) > 0:
            return v
    return None

def getVertexNumbering(visited):
    return {orig: new for new, orig in enumerate(visited)}

def getTraversalSize(matrix):
    degrees = calcSemiDegrees(matrix)
    vertSize = len(getReachable(degrees))
    return vertSize

def bfs(matrix, start):
    matrixSize = len(matrix)
    vertSize = getTraversalSize(matrix)
    queue = [start]
    visited = [start]
    edges = []
    current = start

    while queue:
        current = queue.pop(0)

        if len(visited) == vertSize:
            vertexNumbering = getVertexNumbering(visited)
            treeMatrix = buildTraversalTreeMatrix(matrixSize, edges, vertexNumbering)
            yield {
                'current': None,
                'visited': visited[:],
                'edges': edges[:],
                'treeMatrix': treeMatrix,
                'vertexNumbering': vertexNumbering,
                'end': True
            }

        for i in range(matrixSize):
            if matrix[current][i] == 1 and i not in visited:
                yield {
                    'current': current,
                    'visited': visited[:],
                    'edges': edges[:],
                    'end': False
                }
                visited.append(i)
                edges.append((current, i))
                queue.append(i)

def dfs(matrix, start):
    matrixSize = len(matrix)
    vertSize = getTraversalSize(matrix)
    stack = [start]
    visited = [start]
    edges = []
    current = start

    while stack:
        current = stack[-1]
        found = False

        if len(visited) == vertSize:
            vertexNumbering = getVertexNumbering(visited)
            treeMatrix = buildTraversalTreeMatrix(matrixSize, edges, vertexNumbering)
            yield {
                'current': None,
                'visited': visited[:],
                'edges': edges[:],
                'treeMatrix': treeMatrix,
                'vertexNumbering': vertexNumbering,
                'end': True
            }

        yield {
            'current': current,
            'visited': visited[:],
            'edges': edges[:],
            'end': False
        }

        for i in range(matrixSize):
            if matrix[current][i]:
                if i not in visited:
                    visited.append(i)
                    edges.append((current, i))
                    stack.append(i)
                    found = True
                    break
        if not found:
            stack.pop()
