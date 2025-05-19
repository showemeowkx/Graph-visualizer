import tkinter as tk
from graph import drawGraph

def createMainWin(matrixDir, matrixUndir):
    mainWin = tk.Tk()

    graphOptions = {'r': 200, 'node_r': 25, 'cx':350, 'cy':250}

    mainWin.title("Graph Visualizer")
    mainWin.geometry("800x600")
    mainWin.resizable(0, 0)

    graphLabel = tk.Label(mainWin, text="Directed Graph", font=("Arial", 14, "bold"), pady=10)
    graphLabel.pack()

    isDirected = [1]

    def changeGraph():
        isDirected[0] = 1 - isDirected[0]
        if isDirected[0]:
            drawGraph(canvas, matrixDir, graphOptions, isDirected[0])
            graphLabel.config(text="Directed Graph")
        else:
            drawGraph(canvas, matrixUndir, graphOptions, isDirected[0])
            graphLabel.config(text="Undirected Graph")

    changeGraphBtn = tk.Button(mainWin, text="Change", font=("Helvetica", 11, "italic"), command=changeGraph)
    changeGraphBtn.pack()

    canvas = tk.Canvas(mainWin, width=700, height=500, bg='white')
    canvas.pack()

    drawGraph(canvas, matrixDir, graphOptions, 1)

    return mainWin