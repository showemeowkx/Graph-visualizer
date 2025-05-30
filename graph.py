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

def drawArrow(canvas, x1, y1, x2, y2, offset, mode, color="black", width=1):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx*dx + dy*dy)
    ratio = offset/dist

    x1 += dx * ratio
    y1 += dy * ratio
    x2 -= dx * ratio
    y2 -= dy * ratio

    if mode == 0:
        canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill=color, width=width)
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

        canvas.create_line(x1, y1, ctrlx, ctrly, x2, y2, smooth=True, arrow=tk.LAST, fill=color, width=width)

def drawLoop(canvas, x, y, options, type):
    canvas.create_oval(x + options['offset'], 
                       y - options['loop_r'],
                       x + options['offset'] + (2*options['loop_r']), 
                       y + options['loop_r'])
    if type == 1:
        canvas.create_line(x + options['offset'] + (2*options['loop_r']), y,
                        x + options['offset'] + (2*options['loop_r']) - 5, y - 5,
                        arrow=tk.LAST)
        
def drawParallelEdges(canvas, positions, edges, options, visitedEdges):
    parallelEdges = getParallelEdges(edges)
    edges = [(i,j) for (i,j) in edges if (i,j) not in parallelEdges and (j,i) not in parallelEdges]
    for (x, y) in parallelEdges:
        color = "black"
        width = 1
        if visitedEdges is not None and (x, y) in visitedEdges:
            color = "red"
            width = 3
        x1, y1 = positions[x]
        x2, y2 = positions[y]
        
        drawArrow(canvas, x1, y1, x2, y2, options['node_r'], 1, color, width)
    
    return edges

def drawEdges(canvas, size, positions, edges, options, visitedEdges, type):
    drawn = []
    for (x, y) in edges:
        color = "black"
        width = 1
        if visitedEdges is not None and (x, y) in visitedEdges:
            color = "red"
            width = 3
        elif (x, y) in drawn or (y, x) in drawn:
            continue
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
                drawArrow(canvas, x1, y1, x2, y2, options['node_r'], 0, color, width)
            else: 
                canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

        drawn.append((x, y))

def drawWeights(canvas, positions, edges, visitedEdges, weighted):
    drawn = []
    for (x, y) in edges:
        boxColor = 'white'
        textColor = 'black'
        outlineColor = 'black'

        if visitedEdges is not None and (x, y) in visitedEdges:
            boxColor = 'red'
            textColor = 'white'
            outlineColor = 'white'
        elif (x, y) in drawn or (y, x) in drawn:
            continue

        if x != y:
            x1, y1 = positions[x]
            x2, y2 = positions[y]
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2

            weight = weighted[x][y]
            textId = canvas.create_text(mid_x, mid_y, text=str(weight))
            bbox = canvas.bbox(textId)

            if bbox:
                rectId = canvas.create_rectangle(
                    bbox[0] - 2, bbox[1] - 2, bbox[2] + 2, bbox[3] + 2,
                    outline=outlineColor, fill=boxColor
                )
                canvas.tag_raise(textId, rectId)

            canvas.itemconfig(textId, fill=textColor)
            drawn.append((x, y))


def drawVertices(canvas, positions, options, current, visitedVertices):
    drawn = []
    for i, (x, y) in enumerate(positions):
        color = "lightblue"
        if current is not None:
            if i == current and i not in drawn:
                color = "grey"
                drawn.append(i)
        if visitedVertices is not None:
            if i in visitedVertices and i not in drawn:
                color = "lightgreen"
                drawn.append(i)

        canvas.create_oval(
            x - options['node_r'], y - options['node_r'],
            x + options['node_r'], y + options['node_r'],
            fill=color
        )

        canvas.create_text(x, y, text=str(i+1))

def drawGraph(canvas, matrix, options, type, current=None, visitedEdges=None, visitedVertices=None, weighted=None ):
    canvas.delete("all")
    size = len(matrix)
    positions = calculatePos(size, options['r'], options['cx'], options['cy'])
    edges = getEdgeList(matrix)

    if type == 1:
        edges = drawParallelEdges(canvas, positions, edges, options, visitedEdges)

    drawEdges(canvas, size, positions, edges, options, visitedEdges, type)
    drawVertices(canvas, positions, options, current, visitedVertices)
    if type == 0:
        drawWeights(canvas, positions, edges, visitedEdges, weighted)

