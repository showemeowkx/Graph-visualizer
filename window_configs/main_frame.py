import tkinter as tk
from tkinter import ttk

def createMainFrame(mainWin):
    mainFrame = tk.Frame(mainWin)
    mainFrame.pack(fill="both", expand=True)

    ctrlFrame = tk.Frame(mainFrame, width=700, height=100)
    ctrlFrame.pack()

    ctrlSubFrame = tk.Frame(ctrlFrame, width=675, height=100)
    ctrlSubFrame.pack()

    ctrlSubFrameL = tk.Frame(ctrlSubFrame, width=650, height=10)
    ctrlSubFrameL.pack(side=tk.LEFT, padx=2.5)

    ctrlSubFrameR = tk.Frame(ctrlSubFrame, width=650, height=10)
    ctrlSubFrameR.pack(side=tk.RIGHT, padx=2.5)

    ctrlSubFrameD = tk.Frame(mainFrame, width=650, height=10)
    ctrlSubFrameD.pack(pady=2.5)

    traversalFrame = tk.Frame(mainFrame, width=650, height=10)
    traversalFrame.pack(pady=2.5)

    seedLabel = tk.Label(ctrlSubFrameL, text="Seed:", font=("Arial", 11), anchor="w")
    seedLabel.pack(fill="both")

    seedText = tk.Text(ctrlSubFrameL, width=30, height=1)
    seedText.pack()

    formulaLabel = tk.Label(ctrlSubFrameR, text="Formula:", font=("Arial", 11), anchor="w")
    formulaLabel.pack(fill="both")

    formulaText = tk.Text(ctrlSubFrameR, width=30, height=1)
    formulaText.pack()

    logAnalysisBtn = tk.Button(ctrlSubFrameD, text="Log Analysis", font=("Helvetica", 11), state=tk.DISABLED)
    logAnalysisBtn.pack(padx=2.5, side=tk.LEFT)

    drawCondensationGraphBtn = tk.Button(ctrlSubFrameD, text="Condensation Graph", font=("Helvetica", 11), state=tk.DISABLED)
    drawCondensationGraphBtn.pack(padx=2.5, side=tk.RIGHT)

    generateGraphBtn = tk.Button(ctrlSubFrameD, text="Generate", font=("Helvetica", 11))
    generateGraphBtn.pack(padx=2.5)

    traversalBtn = tk.Button(traversalFrame, text="Start Traversal", font=("Helvetica", 11), state=tk.DISABLED)
    traversalBtn.pack(padx=2.5, side=tk.LEFT)

    traversalBox = ttk.Combobox(traversalFrame, font=("Helvetica", 11), width=5, state='readonly')
    traversalBox.set("BFS")
    traversalBox.pack(padx=2.5, side=tk.RIGHT)

    return seedText, formulaText, logAnalysisBtn, drawCondensationGraphBtn, generateGraphBtn, traversalBtn, traversalBox