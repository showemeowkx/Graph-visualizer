import tkinter as tk
from matrix import stringify

def createMatrixWin(parentWin, matrixDir, matrixUndir):
    matrixWin = tk.Toplevel(parentWin)
    matrixWin.title("Matrices")

    tk.Label(matrixWin, text="Directed matrix:", font=("Arial", 12, "bold"), anchor="w").pack(fill="both", padx=5,pady=5)
    tk.Label(matrixWin, text=stringify(matrixDir, 3), anchor="w").pack(fill="both", padx=5,pady=5)

    tk.Label(matrixWin, text="Undirected matrix:", font=("Arial", 12, "bold"),anchor="w", padx=5, pady=5).pack(fill="both", padx=5,pady=5)
    tk.Label(matrixWin, text=stringify(matrixUndir, 3), anchor="w").pack(fill="both",padx=5,pady=5)
    
    return matrixWin