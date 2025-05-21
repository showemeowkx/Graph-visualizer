from analysis import*
from matrix import stringify

def stringifyType(isDirected):
    typeStr = "\nGraph type: "

    if isDirected == 1:
        typeStr += "Directed"
    else:
        typeStr += "Undirected"

    return typeStr

def stringifySettings(seed, formula):
    return f"\nSeed: {seed}\nFormula: {formula}\n"

def stringifyMatrix(matrix, name):
    return f"\n{name}:\n{stringify(matrix, 3)}\n"

def stringifyDegrees(matrix, mode):
    degreesStr = 'Degrees:\n'
    size = len(matrix)
    degrees = calcDegrees(matrix, mode)
    for i in range(size):
        degreesStr += f"({i+1}) -> {degrees[i]}\n"

    if mode == 1:
        semiDegrees = calcSemiDegrees(matrix)
        ins = semiDegrees['in']
        outs = semiDegrees['out']
        semiDegreesInStr = "\nDegrees (IN):\n"
        semiDegreesOutStr = "\nDegrees (OUT):\n"

        for i in range(size):
            semiDegreesInStr += f"({i+1}) -> {ins[i]}\n"
            semiDegreesOutStr += f"({i+1}) -> {outs[i]}\n"
        
        degreesStr += semiDegreesInStr
        degreesStr += semiDegreesOutStr

    return degreesStr

def stringifyValueOrNo(matrix, mode, name, trueText, falseText, valueRequired, callback):
    string = f"\n{name}: "
    degrees = calcDegrees(matrix, mode)
    recieved = callback(degrees)

    if recieved:
        if valueRequired == 1:
            string += trueText + f" {recieved}\n"
        else:
            string += trueText + "\n"
    else:
        string += falseText + "\n"

    return string

def stringifyPaths(matrix, length):
    pathsStr = f"\nPaths ({length}):\n"
    pathsDict = buildPathsDict(matrix, length)

    for edges, paths in pathsDict.items():
        pathsStr += edges + ":\n"
        pathStr = ""

        for path in paths:
            intermidiatePath = ""
            index = 0
            for vert in path:
                intermidiatePath += f"{vert}"
                if index < len(path) - 1:
                    intermidiatePath += " -> "
                else:
                    intermidiatePath += "\n"
                index += 1

            pathStr += "\t" + intermidiatePath

        pathsStr += pathStr + "\n"

    return pathsStr

def stringifyComponents(matrix):
    componentsStr = "\nStrong components: "
    components = getStrongComponents(matrix)
    for component in components:
        componentsStr += f"{component} "

    componentsStr += "\n\n"

    return componentsStr

def stringifyVertexNumbering(vertexNumbering):
    vertexNumberingStr = "\nVertex numbering: "
    for key, value in vertexNumbering.items():
        vertexNumberingStr += f"\n({key+1}) -> {value+1}"

    vertexNumberingStr += "\n"

    return vertexNumberingStr
