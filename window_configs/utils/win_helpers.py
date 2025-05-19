import tkinter as tk
from window_configs.utils.log_builder import*

def disableComponnets(components):
    for component in components:
        component.config(state=tk.DISABLED)

def enableComponnets(components):
    for component in components:
        component.config(state=tk.NORMAL)

def validateSeedText(seed):
    if len(seed) > 4 or len(seed) < 4:
        return False
    
    seedNums = [int(num) for num in seed]

    return seedNums

def validateFormulaText(formula):
    formulaTemp = formula
    for i in range(4):
        formulaTemp = formulaTemp.replace(f"n{i+1}", "1")
        
    try:
        if type(eval(formulaTemp)) is float or type(eval(formulaTemp)) is int:
            return formula
        else: 
            return False
        
    except: 
        return False
    
def showComponents(components):
    componentsStr = ""
    for index, component in enumerate(components):
        componentsStr += f"({index+1}) -> {component}; "

    return componentsStr
    
def analyzeGraph(matrix, seed, formula, mode):
    graphType = stringifyType(mode)
    settings = stringifySettings(seed, formula)
    adjancency = stringifyMatrix(matrix, "Adjancency matrix")
    degrees = stringifyDegrees(matrix, mode)
    regular = stringifyValueOrNo(matrix, mode, "Regular", "Yes | Degree:", "No", 1, isRegular)
    isolated = stringifyValueOrNo(matrix, mode, "Isolated vertices", "", "None", 1, getIsolated)
    leaves = stringifyValueOrNo(matrix, mode, "Leaves", "", "None", 1, getLeaves)
    doublePaths = stringifyPaths(matrix, 2)
    tripplePaths = stringifyPaths(matrix, 3)
    reach = buildReachabilityMatrix(matrix)
    reachStr = stringifyMatrix(reach, "Reachability matrix")
    strong = buildStrongConnectivityMatrix(reach)
    strongStr = stringifyMatrix(strong, "Strong connection matrix")
    components = stringifyComponents(matrix)
    condensation = buildCondensationMatrix(matrix)
    condensationStr = stringifyMatrix(condensation, "Condensation matrix")

    analysis = "GRAPH ANALYSIS:\n"+graphType+settings+adjancency+degrees+regular+isolated+leaves+doublePaths+tripplePaths+reachStr+strongStr+components+condensationStr

    return analysis