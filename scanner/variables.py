from collections import deque


def init(): 
    global line 
    global column
    global lastToken 
    global error
    global fileLines
    global semanticStack
    global lineInserted
    global tmpCounter

    lastToken = [0,0]
    line = 0
    column = 0
    error = False
    fileLines = []
    semanticStack = deque()
    lineInserted = 0
    tmpCounter = 0