from analysis import buildTraversalTreeMatrix
import math

def findStartVertex(matrix, visited=[]):
    size = len(matrix)
    for v in range(size):
        if v not in visited and sum(matrix[v]) > 0:
            return v
    return None

def getVertexNumbering(visited):
    return {orig: new for new, orig in enumerate(visited)}

def bfs(matrix, start):
    size = len(matrix)
    queue = [start]
    visited = [start]
    edges = []

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

def mst(matrix, start):
    size = len(matrix)
    selected = [start]
    edges = []
    weightSum = 0

    while len(selected) != size:
        min = math.inf
        row = 0
        col = 0

        for i in range(size):
            if i in selected:
                for j in range(size):
                    if j not in selected and matrix[i][j]:
                        if min > matrix[i][j]:
                            min = matrix[i][j]
                            row = i
                            col = j

        if min == math.inf:
            break

        yield {
            'current': row,
            'visited': selected[:],
            'edges': edges[:],
            'end': False
        }

        weightSum += min
        edges.append((row, col))
        selected.append(col)
    
    yield {
        'current': None,
        'visited': selected[:],
        'edges': edges[:],
        'sum': weightSum,
        'end': True
    }



