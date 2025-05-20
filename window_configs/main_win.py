import tkinter as tk
from matrix import fillMatrix, convertMatrix
from graph import drawGraph
from window_configs.main_frame import createMainFrame
from traversal import*
from window_configs.utils.log_file import*
from window_configs.utils.win_helpers import*

def createMainWin():
    mainWin = tk.Tk()

    graphOptions = {'r': 200, 'node_r': 25, 'cx':350, 'cy':250}

    mainWin.title("Graph Visualizer")
    mainWin.geometry("800x725")
    mainWin.resizable(0, 0)

    isDirected = [1]
    isCondensation = [0]
    logPath = initDir()

    def changeGraph():
        isDirected[0] = 1 - isDirected[0]
        if isDirected[0]:
            traversalBtn.config(state=tk.NORMAL)
            drawGraph(canvas, matrixDir, graphOptions, isDirected[0])
            graphLabel.config(text="Directed Graph")
        else:
            traversalBtn.config(state=tk.DISABLED)
            drawGraph(canvas, matrixUndir, graphOptions, isDirected[0])
            graphLabel.config(text="Undirected Graph")

    def generateGraph():
        seedNums = validateSeedText(seedText.get("1.0", "end-1c"))
        formula = validateFormulaText(formulaText.get("1.0", "end-1c"))

        if seedNums and formula:
            global matrixDir, matrixUndir, strongComponentsStr

            isDirected[0] = 1
            components = [generateGraphBtn, changeGraphBtn, logAnalysisBtn, drawCondensationGraphBtn, traversalBtn, seedText, formulaText, startText]
            enableComponnets(components)
            graphLabel.config(text="Directed Graph")
            changeGraphBtn.config(text="Change", command=changeGraph)
            matrixDir = fillMatrix(seedNums[0], seedNums[1], seedNums[2], seedNums[3], formula)
            matrixUndir = convertMatrix(matrixDir)

            drawGraph(canvas, matrixDir, graphOptions, 1)

    def logAnalysis():
        if isDirected[0] == 0:
            mode = 0
            matrix = matrixUndir
        else:
            mode = 1
            matrix = matrixDir

        seed = seedText.get("1.0", "end-1c")
        formula = formulaText.get("1.0", "end-1c")
        logText = analyzeGraph(matrix, seed, formula, mode)
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
            else:
                global dfsGen
                traversalMode = ["DFS"]
                dfsGen = dfs(matrixDir, start)
                nextStep()

    def nextStep():
        if traversalMode[0] == "BFS":
            try:
                step = next(bfsGen)
                drawGraph(canvas, matrixDir, graphOptions, 1, step['current'], step['edges'], step['visited'])
                if step['end']:
                    changeGraphBtn.config(text="Stop")
                    changeGraphBtn.config(command=generateGraph)
            except StopIteration:
                changeGraphBtn.config(text="Stop")
                changeGraphBtn.config(command=generateGraph)
        else:
            try:
                step = next(dfsGen)
                drawGraph(canvas, matrixDir, graphOptions, 1, step['current'], step['edges'], step['visited'])
                if step['end']:
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
    traversalBox.config(values=["BFS", "DFS"])
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