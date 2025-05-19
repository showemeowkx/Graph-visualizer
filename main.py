from matrix import fillMatrix, convertMatrix
from window_configs import matrix_win, main_win

matrixDir = fillMatrix(4, 3, 3, 1)
matrixUndir = convertMatrix(matrixDir)

mainWin = main_win.createMainWin(matrixDir, matrixUndir)
matrixWin = matrix_win.createMatrixWin(mainWin, matrixDir, matrixUndir)

mainWin.mainloop()
matrixWin.mainloop()