from analysis import getReachable, calcSemiDegrees, buildTraversalTreeMatrix

def findStartVertex(matrix, visited=[]):
    size = len(matrix)
    for v in range(size):
        if v not in visited and sum(matrix[v]) > 0:
            return v
    return None

def getVertexNumbering(visited):
    return {orig: new for new, orig in enumerate(visited)}

def getTraversalSize(matrix):
    degrees = calcSemiDegrees(matrix)
    vertSize = len(getReachable(degrees))
    return vertSize

def bfs(matrix, start):
    size = len(matrix)
    queue = [start]
    visited = [start]
    edges = []
    current = start

    while queue or start is not None:
        current = queue.pop(0)

        if len(visited) == size or start is None:
            vertexNumbering = getVertexNumbering(visited)
            treeMatrix = buildTraversalTreeMatrix(size, edges)
            yield {
                'current': None,
                'visited': visited[:],
                'edges': edges[:],
                'treeMatrix': treeMatrix,
                'vertexNumbering': vertexNumbering,
                'end': True
            }

        for i in range(size):
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

        start = findStartVertex(matrix, visited)

def dfs(matrix, start):
    size = len(matrix)
    stack = [start]
    visited = [start]
    edges = []
    current = start

    while stack or start is not None:
        current = stack[-1]
        found = False

        if len(visited) == size or start is None:
            vertexNumbering = getVertexNumbering(visited)
            treeMatrix = buildTraversalTreeMatrix(size, edges)
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

        for i in range(size):
            if matrix[current][i]:
                if i not in visited:
                    visited.append(i)
                    edges.append((current, i))
                    stack.append(i)
                    found = True
                    break
        if not found:
            stack.pop()

        start = findStartVertex(matrix, visited)
