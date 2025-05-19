import os
import time

def initDir():
    path = "./logs"

    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path

def addLogFile(seed, path, log):
    filename = f"{seed}_{time.time()}.txt"
    filePath = f"{path}/{filename}"
    logFile =  open(filePath, "x")
    logFile.write(log)
    
    print(f"Logged to {filePath} successfully!")