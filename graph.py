import math
import tkinter as tk
from matrix import getEdgeList

def calculatePos(n, r, cx, cy):
    positions = []
    for i in range(n):
        angle = (2*math.pi) * (i/n)
        x = cx + (r*math.cos(angle))
        y = cy + (r*math.sin(angle))
        positions.append((x, y))

    return positions

def drawArrow(canvas, x1, y1, x2, y2, offset):
    dx = x2 - x1
    dy = y2 - y1
    ratio = offset/math.sqrt(dx*dx + dy*dy)

    x1 += dx * ratio
    y1 += dy * ratio
    x2 -= dx * ratio
    y2 -= dy * ratio

    canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)

def drawLoop(canvas, x, y, options, type):
    canvas.create_oval(x + options['offset'], 
                       y - options['loop_r'],
                       x + options['offset'] + (2*options['loop_r']), 
                       y + options['loop_r'])
    if type == 1:
        canvas.create_line(x + options['offset'] + (2*options['loop_r']), y,
                        x + options['offset'] + (2*options['loop_r']) - 5, y - 5,
                        arrow=tk.LAST)

def drawGraph(canvas, matrix, options, type):
    canvas.delete("all")
    size = len(matrix)
    positions = calculatePos(size, options['r'], options['cx'], options['cy'])
    edges = getEdgeList(matrix)

    for (x, y) in edges:
        if x == y:
            x0, y0 = positions[x]
            if x <= round(size*0.25) or x >= round(size*0.75):
                loopOptions = {'offset': options['node_r']/2, 'loop_r': options['node_r']*0.75}
            else:
                loopOptions = {'offset': -options['node_r']/2, 'loop_r': -options['node_r']*0.75}
            drawLoop(canvas, x0, y0, loopOptions, type)
        else:
            x1, y1 = positions[x]
            x2, y2 = positions[y]
            if type == 1:
                drawArrow(canvas, x1, y1, x2, y2, options['node_r'])
            else: canvas.create_line(x1, y1, x2, y2)

    for i, (x, y) in enumerate(positions):
        canvas.create_oval(
            x - options['node_r'], y - options['node_r'],
            x + options['node_r'], y + options['node_r'],
            fill="lightblue"
        )

        canvas.create_text(x, y, text=str(i+1))