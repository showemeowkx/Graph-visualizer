import math
import tkinter as tk
from matrix import getEdgeList, getParallelEdges
from analysis import *
from window_configs.utils.log_builder import*

def calculatePos(n, r, cx, cy):
    positions = []
    for i in range(n):
        angle = (2*math.pi) * (i/n)
        x = cx + (r*math.cos(angle))
        y = cy + (r*math.sin(angle))
        positions.append((x, y))

    return positions

def drawArrow(canvas, x1, y1, x2, y2, offset, mode):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx*dx + dy*dy)
    ratio = offset/dist

    x1 += dx * ratio
    y1 += dy * ratio
    x2 -= dx * ratio
    y2 -= dy * ratio

    if mode == 0:
        canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
    else:
        dx = dx / dist
        dy = dy / dist

        midx = dy
        midy = -dx
        norm = math.sqrt(midx*midx + midy*midy)

        midx = midx / norm
        midy = midy / norm

        ctrlx = (x1 + x2) / 2 + midx * offset
        ctrly = (y1 + y2) / 2 + midy * offset

        canvas.create_line(x1, y1, ctrlx, ctrly, x2, y2, smooth=True, arrow=tk.LAST)

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

    if type == 1:
        parallelEdges = getParallelEdges(edges)
        edges = [(i,j) for (i,j) in edges if (i,j) not in parallelEdges and (j,i) not in parallelEdges]
        for (x, y) in parallelEdges:
            x1, y1 = positions[x]
            x2, y2 = positions[y]
            drawArrow(canvas, x1, y1, x2, y2, options['node_r'], 1)

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
                drawArrow(canvas, x1, y1, x2, y2, options['node_r'], 0)
            else: canvas.create_line(x1, y1, x2, y2)

    for i, (x, y) in enumerate(positions):
        canvas.create_oval(
            x - options['node_r'], y - options['node_r'],
            x + options['node_r'], y + options['node_r'],
            fill="lightblue"
        )

        canvas.create_text(x, y, text=str(i+1))
