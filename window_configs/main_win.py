import tkinter as tk
from matrix import fillMatrix, convertMatrix
from graph import drawGraph
from window_configs.main_frame import createMainFrame
from traversal import*
from window_configs.utils.log_file import*
from window_configs.utils.win_helpers import*

def createMainWin():
    global treeMatrix, vertexNumbering, weightSum
    mainWin = tk.Tk()

    graphOptions = {'r': 200, 'node_r': 25, 'cx':350, 'cy':250}

    mainWin.title("Graph Visualizer")
    mainWin.geometry("800x725")
    mainWin.resizable(0, 0)

    isDirected = [1]
    isCondensation = [0]
    logPath = initDir()

    treeMatrix = None
    vertexNumbering = None
    weightSum = None

    def changeGraph():
        global matrixWeight
        isDirected[0] = 1 - isDirected[0]
        if isDirected[0]:
            startText.config(state=tk.NORMAL)
            traversalBox.config(values=["BFS", "DFS"])
            traversalBox.set("BFS")
            graphOptions['node_r'] = 25
            drawGraph(canvas, matrixDir, graphOptions, isDirected[0])
            graphLabel.config(text="Directed Graph")
        else:
            startText.delete("1.0", "end-1c")
            startText.config(state=tk.DISABLED)
            traversalBox.config(values="MST")
            traversalBox.set("MST")
            graphOptions['node_r'] = 15
            drawGraph(canvas, matrixUndir, graphOptions, isDirected[0], weighted=matrixWeight)
            graphLabel.config(text="Undirected Graph")

    def generateGraph():
        seed = seedText.get("1.0", "end-1c")
        seedNums = validateSeedText(seed)
        formula = validateFormulaText(formulaText.get("1.0", "end-1c"))

        if seedNums and formula:
            global matrixDir, matrixUndir, matrixWeight
            isDirected[0] = 1
            components = [generateGraphBtn, changeGraphBtn, logAnalysisBtn, drawCondensationGraphBtn, traversalBtn, seedText, formulaText, startText]
            enableComponnets(components)
            graphLabel.config(text="Directed Graph")
            changeGraphBtn.config(text="Change", command=changeGraph)
            traversalBox.config(values=["BFS", "DFS"])
            traversalBox.set("BFS")
            matrixDir = fillMatrix(seedNums[0], seedNums[1], seedNums[2], seedNums[3], formula)
            matrixUndir = convertMatrix(matrixDir)
            matrixWeight = fillWeightedMatrix(matrixUndir, seed)

            graphOptions['node_r'] = 25
            drawGraph(canvas, matrixDir, graphOptions, 1)

    def logAnalysis():
        global matrixDir, matrixUndir, treeMatrix, vertexNumbering, matrixWeight, weightSum
        if isDirected[0] == 0:
            mode = 0
            matrix = matrixUndir
        else:
            mode = 1
            matrix = matrixDir
            matrixWeight = None

        seed = seedText.get("1.0", "end-1c")
        formula = formulaText.get("1.0", "end-1c")
        logText = analyzeGraph(matrix, seed, formula, mode, treeMatrix, vertexNumbering, matrixWeight, weightSum)
        addLogFile(seed, logPath, logText)
        
    def drawCondensationGraph():
        components = [changeGraphBtn, logAnalysisBtn, seedText, formulaText, startText, traversalBtn]
        if isCondensation[0] == 0:
            matrixCond = buildCondensationMatrix(matrixDir)
            graphLabel.config(text="Condensation Graph")
            drawCondensationGraphBtn.config(text="Back to Directed")
            disableComponnets(components)
            isCondensation[0] = 1
            drawGraph(canvas, matrixCond, graphOptions, 1)
            strongComponentsStr = showComponents(getStrongComponents(matrixDir))
            strongComponentsLabel.config(text=f"{strongComponentsStr}")
            changeGraphBtn.pack_forget()
            strongComponentsLabel.pack(pady=5)
        else:
            graphLabel.config(text="Directed Graph")
            drawCondensationGraphBtn.config(text="Condensation Graph")
            enableComponnets(components)
            isDirected[0] = 1
            isCondensation[0] = 0
            drawGraph(canvas, matrixDir, graphOptions, 1)
            strongComponentsLabel.pack_forget()
            changeGraphBtn.pack(pady=5)

    def startTraversal():
        start = validateStartText(startText.get("1.0", "end-1c"), matrixDir)
        if start is not None:
            global traversalMode
            components = [generateGraphBtn, logAnalysisBtn, drawCondensationGraphBtn, traversalBtn, seedText, formulaText, startText]
            disableComponnets(components)
            graphLabel.config(text=f"[{traversalBox.get()}] Traversal...")
            changeGraphBtn.config(text="Next")
            changeGraphBtn.config(command=nextStep)
            if traversalBox.get() == "BFS":
                global bfsGen
                traversalMode = ["BFS"]
                bfsGen = bfs(matrixDir, start)
                nextStep()
            elif traversalBox.get() == "DFS":
                global dfsGen
                traversalMode = ["DFS"]
                dfsGen = dfs(matrixDir, start)
                nextStep()
            else:
                global mstGen
                traversalMode = ["MST"]
                mstGen = mst(matrixWeight, start)
                nextStep()

    def nextStep():
        try:
            mode = traversalMode[0]
            if mode == "BFS" or mode == "DFS":
                step = next(bfsGen) if mode == "BFS" else next(dfsGen)
                drawGraph(canvas, matrixDir, graphOptions, 1, step['current'], step['edges'], step['visited'])
                if step['end']:
                    global treeMatrix, vertexNumbering
                    treeMatrix = step['treeMatrix']
                    vertexNumbering = step['vertexNumbering']
                    changeGraphBtn.config(text="Stop")
                    changeGraphBtn.config(command=generateGraph)
            else:
                step = next(mstGen)
                drawGraph(canvas, matrixUndir, graphOptions, 0, step['current'], step['edges'], step['visited'], matrixWeight)
                if step['end']:
                    global weightSum
                    weightSum = step['sum']
                    changeGraphBtn.config(text="Stop")
                    changeGraphBtn.config(command=generateGraph)
        except StopIteration:
            changeGraphBtn.config(text="Stop")
            changeGraphBtn.config(command=generateGraph)

    graphLabel = tk.Label(mainWin, text="Generate Graph", font=("Arial", 14, "bold"), pady=10)
    graphLabel.pack(pady=5)

    seedText, formulaText, logAnalysisBtn, drawCondensationGraphBtn, generateGraphBtn, startText, startLabel, traversalBtn, traversalBox = createMainFrame(mainWin)

    validateStartTextLength(startText, 2)
    validateStartTextLength(seedText, 4)
    logAnalysisBtn.config(command=logAnalysis)
    drawCondensationGraphBtn.config(command=drawCondensationGraph)
    generateGraphBtn.config(command=generateGraph)
    traversalBtn.config(command=startTraversal)

    canvas = tk.Canvas(mainWin, width=700, height=500, bg='white')
    canvas.pack()

    strongComponentsLabel = tk.Label(mainWin, text="", font=("Consolas", 9), pady=2.5)

    changeGraphBtn = tk.Button(mainWin, text="Change", font=("Helvetica", 11, "italic"), pady=2.5, command=changeGraph, state=tk.DISABLED)
    changeGraphBtn.pack(pady=5)

    return mainWin