## ------------------------------------------------------------------------------------------
#                                   8 - Puzzle Solver [BFS]
## ------------------------------------------------------------------------------------------

# Author: Jai Sharma
# Course: ENPM661 - Planning
# Assignment: Project 1

## ------------------------------------------------------------------------------------------
#                                        Import Libraries
## ------------------------------------------------------------------------------------------

import numpy as np
import ast
import time

start_time = time.time()
print("=======================================================================")


## ------------------------------------------------------------------------------------------
#                                     Start and Goal States
## ------------------------------------------------------------------------------------------

# Start State
s = [1,4,2,
     6,7,3,
     5,0,8]
# Goal State
g = [1,2,3,
     4,5,6,
     7,8,0]

Node_State_i = []
Parent_State_i = []
back_track = {}     # collects information in dictionary format
Parent_State_i.append([s])
goal_reached = 0
totalTime = 0 # measure total execution time

# function to find location of blank tile in current 3x3 matrix as [i,j]
def blank_loc(cur_node):
    cur_node=np.reshape(cur_node,(3,3))
    for row in range(0,3,1):
        for col in range(0,3,1):
            if cur_node[row][col] == 0:
                i = row
                j = col          
    return([i,j])

# function to convert 1x9 list to 3x3 matrix, for display
def list2matrix(inp_list):  
    matrix = []
    while inp_list != []:
        matrix.append(inp_list[:3])
        inp_list = inp_list[3:]
    matrix=np.reshape(matrix,(3,3)) #reshaping to a 3 by 3 matrix
    return(matrix)

# function to convert 3x3 matrix (data elements) to 1x9 list, flatten the list
def matrix2list(matrix):
    newlist = []
    for i in matrix[0].tolist():
            newlist += i
    return newlist

## ------------------------------------------------------------------------------------------
#                                         Action Moves
## ------------------------------------------------------------------------------------------

# functions for --> ActionMoveLeft,ActionMoveRight, ActionMoveUp, ActionMoveDown

def ActionMoveLeft(CurrentNode): # Swap tile with what's on Left
    row, col = blank_loc(CurrentNode)[0], blank_loc(CurrentNode)[1]
    if col!=0:    
        CurrentNode[row][col-1],CurrentNode[row][col] = CurrentNode[row][col],CurrentNode[row][col-1]
        return(CurrentNode,True)    # Left is possible
    else:          
        return(CurrentNode,False)   # Left not possible
    
def ActionMoveRight(CurrentNode): # Swap tile with what's on Right
    row, col = blank_loc(CurrentNode)[0], blank_loc(CurrentNode)[1]
    if col!=2:    
        CurrentNode[row][col],CurrentNode[row][col+1] = CurrentNode[row][col+1],CurrentNode[row][col]
        return(CurrentNode,True)    # Right is possible
    else:          
        return(CurrentNode,False)   # Right not possible

def ActionMoveUp(CurrentNode): # Swap tile with what's Up
    row, col = blank_loc(CurrentNode)[0], blank_loc(CurrentNode)[1]
    if row!=0:  
        CurrentNode[row][col],CurrentNode[row-1][col] = CurrentNode[row-1][col],CurrentNode[row][col]
        return(CurrentNode,True)    # Up is possible
    else:          
        return(CurrentNode,False)   # Up not possible
    
def ActionMoveDown(CurrentNode): # Swap tile with what's Down
    row, col = blank_loc(CurrentNode)[0], blank_loc(CurrentNode)[1]
    if row!=2:   
        CurrentNode[row][col],CurrentNode[row+1][col] = CurrentNode[row+1][col],CurrentNode[row][col]
        return(CurrentNode,True)    # Down is possible
    else:          
        return(CurrentNode,False)   # Down not possible

## ------------------------------------------------------------------------------------------
#                                     BFS Path Generation
## ------------------------------------------------------------------------------------------

# back tracking function --> generate_path

def generate_path(s,g): # only used to compute forward BFS path
    Node_State_i.append(s)
    global goal_reached 
    if s==g: 
        print('\n')
        print('|| At Goal Position Already ||')
    else: 
        Parent_Node_Index_i=1
        for element in Parent_State_i: 
            if goal_reached==[]:    
                break
            else:
                Parent_State_i.append([]) 
                print('Computing Paths in Layer # ', Parent_Node_Index_i)

                for Node_Index_i in element: # around every element in every list
                    # sequence to check --> left, up, right, down
                    # Makes a copy of matrix, to pass through 'Action Move' functions
                    left_copy = up_copy = right_copy = down_copy = Node_Index_i.copy()       
                    
                    # Performs tile swapping in each direction [if viable]
                    left=matrix2list(ActionMoveLeft(list2matrix(Node_Index_i.copy())))  
                    up=matrix2list(ActionMoveUp(list2matrix(Node_Index_i.copy())))
                    right=matrix2list(ActionMoveRight(list2matrix(Node_Index_i.copy())))
                    down=matrix2list(ActionMoveDown(list2matrix(Node_Index_i.copy())))
                    
                    back_track[str(left_copy)] = [] #Adding a new empty value for the 
                    #new Parent Node Key
                    
                    # Checks if the step is explored
                    if left not in Node_State_i :
                        back_track[str(left_copy)].append(left)
                    if left_copy!=up_copy: 
                        back_track[str(up_copy)] = []
                    if up not in Node_State_i : 
                        back_track[str(up_copy)].append(up)
                    if up_copy!=right_copy: 
                        back_track[str(right_copy)] = []
                    if right not in Node_State_i : 
                        back_track[str(right_copy)].append(right)
                    if right_copy!=down_copy: 
                        back_track[str(down_copy)] = []
                    if down not in Node_State_i : 
                        back_track[str(down_copy)].append(down)

                    # adds to dictionary if the pattern is not explored yet, 
                    # global node, parent node updated
                    if left not in Node_State_i :
                        Node_State_i.append(left)
                        Parent_State_i[Parent_Node_Index_i].append(left)
                    if up not in Node_State_i:
                        Node_State_i.append(up)
                        Parent_State_i[Parent_Node_Index_i].append(up)
                    if right not in Node_State_i: 
                        Node_State_i.append(right)
                        Parent_State_i[Parent_Node_Index_i].append(right)
                    if down not in Node_State_i: 
                        Node_State_i.append(down)
                        Parent_State_i[Parent_Node_Index_i].append(down)
                
                # Check if Current State is Goal State
                for output in Node_State_i: 
                    if output==g: 
                        print("=======================================================================")
                        print('\n') 
                        print('|| GOAL REACHED ||')           
                        goal_reached=[] 

            Parent_Node_Index_i += 1 

    
# call function to compute BFS path
generate_path(s,g) 


## ------------------------------------------------------------------------------------------
#                                      Backtracking
## ------------------------------------------------------------------------------------------

# start at goal state and track the moves back to start node state

start = g
goal = s
back_track_path = [] # stores the elements of the back-tracked path

while start!=goal:
    for keys, values in back_track.items():   # dictionary search syntax
        while start in values:
            keys= ast.literal_eval(keys)     
            start = keys                     
            back_track_path.append(start)    # builds the backtracking list

back_track_path=back_track_path[::-1] #reversing the list
back_track_path.append(g) 

transposed_list = [] 
for i in back_track_path:
    matrix = list2matrix(i) 
    matrix = matrix.transpose()
    var=[]
    for i in matrix:
        for j in i:
            var.append(j)
    transposed_list.append(var) 

## ------------------------------------------------------------------------------------------
#                                Display Forward Path
## ------------------------------------------------------------------------------------------

# Forward Path
print('\n')
print("=======================================================================")
print(' Forward Path: START ----> GOAL ')
print("=======================================================================")
print('\n')
print('Start State')
print('\n')

for i in back_track_path:
    print(list2matrix(i))
    print('\n')

print('Goal State')
print('\n')


# Print Execution Time

end_time = time.time()
print("=======================================================================")
print("Time to Solve Puzzle:", round((end_time - start_time), 3), "seconds")
print("=======================================================================")

print('\n')
