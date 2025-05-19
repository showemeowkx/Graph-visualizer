import tkinter as tk

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
    ctrlSubFrameD.pack(pady=5)

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

    return seedText, formulaText, logAnalysisBtn, drawCondensationGraphBtn, generateGraphBtn