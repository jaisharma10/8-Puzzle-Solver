## ------------------------------------------------------------------------------------------
#                                   8 - Puzzle Solver [BFS]
## ------------------------------------------------------------------------------------------

'''
Author: Jai Sharma
Task: implement Breath First Search [BFS] algorithm to solve an 8-puzzle problem

'''

## ------------------------------------------------------------------------------------------
#                                        Import Libraries
## ------------------------------------------------------------------------------------------

import numpy as np
import time
import copy
from collections import deque

start_time = time.time()
print("=======================================================================")

## ------------------------------------------------------------------------------------------
#                                     Node Class
## ------------------------------------------------------------------------------------------

class Node:
    
    '''
    Attributes:
        state: state of the node
        parent: parent of the node
    '''
    
    def __init__(self, state, parent):
        self.state = state     # current state of the puzzle
        self.parent = parent    # stores parent of current state
        
    def __repr__(self):         # special method used to represent a class’s objects as string
        return str(self.state)  
    
    def blankTile(self): # find location of blank tile in current 3x3 matrix as [i,j]
        for row in range(0,3,1):
            for col in range(0,3,1):
                # print("self.state:",self.state)
                if self.state[row][col] == 0:
                    i = row
                    j = col 
                    return([i,j])
    
    # functions for --> moveLeft, moveRight, ActionMoveUp, ActionMoveDown
    
    def moveUp(self, tile): # Swap tile with the tile Above
        row, col = tile[0], tile[1]
        if row != 0:  # tile above exists
            currentNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  # parent is also a Node in form (state, parent)
            currentNode.state[row][col], currentNode.state[row-1][col]  = currentNode.state[row-1][col], currentNode.state[row][col]
            # print("up -->", currentNode.state)
            return(currentNode)    # Up is possible
        else:
            return(False)       # Up not possible
    
    def moveDown(self, tile): # Swap tile with the tile Below
        row, col = tile[0], tile[1]
        if row != 2:  # tile below exists
            currentNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent)) 
            currentNode.state[row][col], currentNode.state[row+1][col]  = currentNode.state[row+1][col], currentNode.state[row][col]
            # print("down -->", currentNode.state)    
            return(currentNode)    # Down is possible         
        else:
            return(False)       # Down not possible

    def moveLeft(self, tile): # Swap tile with the tile on Left
        row, col = tile[0], tile[1]
        if col != 0:  # tile to right exists
            currentNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  
            currentNode.state[row][col], currentNode.state[row][col-1]  = currentNode.state[row][col-1], currentNode.state[row][col]
            # print("left -->", currentNode.state)
            return(currentNode)    # Left is possible
        else:       
            return(False)       # Left not possible

    def moveRight(self, tile): # Swap tile with the tile on Right
        row, col = tile[0], tile[1]
        if col != 2: # tile to left exists
            currentNode = Node(copy.deepcopy(self.state), Node(self.state, self.parent))  
            currentNode.state[row][col], currentNode.state[row][col+1]  = currentNode.state[row][col+1], currentNode.state[row][col]
            # print("Right -->", currentNode.state)
            return(currentNode)    # Right is possible         
        else:
            return(False)       # Right not possible
    
    def getNeighbours(self, tile): # check for neighbours in the 4 directions
        neighbours = []
        up = self.moveUp(tile)
        down = self.moveDown(tile)
        left = self.moveLeft(tile)
        right = self. moveRight(tile)
      
        neighbours.append(up) if up else None
        neighbours.append(down) if down else None
        neighbours.append(left) if left else None
        neighbours.append(right) if right else None
        
        return(neighbours)

## ------------------------------------------------------------------------------------------
#                                         BFS Function
## ------------------------------------------------------------------------------------------

def bfs(s, g):
    
    counter = 0
    n = 1
    
    startNode = Node(s, None)
    queue = deque()               # all neighbour states to explore
    visitedList = []              # all visited states

    # add start node to visited list and queue
    queue.append(startNode)    
    visitedList.append(startNode)

    while queue != []:
        currentNode = queue.popleft()  # pop last node 

        if currentNode.state not in visitedList:         # new state is not goal state and not in visited list
            visitedList.append(currentNode.state)
            if currentNode.state == g:  # check if goal state reached
                print("Goal Reached! Backtracked Path is:") 
                backtrack(currentNode, startNode)
                break
            else: # if not goal, add neigbours to queue
                zeroTile = currentNode.blankTile()
                Neighbours = currentNode.getNeighbours(zeroTile)  # get next layer
                for child in Neighbours:
                    if child not in queue:
                        queue.append(child)

    return(None)
        
        
## ------------------------------------------------------------------------------------------
#                                  Backtracking Function
## ------------------------------------------------------------------------------------------

def backtrack(current, start):
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    # print("G:", str(current.row_to_col_notation()))  # backtrack to start node
    print("G:", current.state)  # backtrack to start node
    while(current.state != start.state):
        current = current.parent
        print(current.state)
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    return(None)
        
## ------------------------------------------------------------------------------------------
#                                       Main Function
## ------------------------------------------------------------------------------------------

if __name__== "__main__":
    
    # Start State
    s = [ [2,1,3],
          [4,7,5],
          [6,0,8] ]
    
    # Goal State
    
    g = [ [1,2,3],
          [4,5,6],
          [7,8,0] ]

    if s == g: # Check if start node is goal node
        print("Start node is Goal Node!!")
    else: 
        bfs(s, g)
    
## ------------------------------------------------------------------------------------------
#                                Display --> Forward and Backward Path
## ------------------------------------------------------------------------------------------

end_time = time.time()

print("=======================================================================")
print("Time to Solve 8-Puzzle Problem:", round((end_time - start_time), 3), "seconds")
print("=======================================================================")

print('\n')
