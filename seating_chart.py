# Andrew Byrne
# 04/01/2025
# Seating Chart

import numpy as np
from numpy import random

if __name__=='__main__':
    #input functions
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    #creates an empty array
    grid = np.array ( [] )
    nameList = ["Andrew", "Ben", "Ethan", "Hannah", "Jalen", "Venus", "Edison", "Chase", "Will", "Chris", "Bob", "Nick", "Ava"]
    #adds error if not enough people
    if len(nameList) < rows * columns:
        print(" Not enough names in the list for this classroom size.")
        exit()
    #loops though the number of rows and columns of the classrooms size
    for i in range(rows):
        for j in range(columns):
            randName = np.random.choice(nameList)
            #append randName to grid
            grid= np.append(grid, f"{randName} ({i}, {j})")
            #remove randName from randList
            nameList.remove(randName)
    # reshaping the grid
    grid = grid.reshape(rows,columns)
    #formats the names and index
    for i in range(rows):
        for j in range(columns):
            if j < columns -1:
                print(grid[i, j], end=" ")
            else:
                print(grid[i, j], end="\n")
   # for i in range(rows):
       # row_display = "  ".join([f'{grid[i, j]} ({i},{j})' for j in range(columns)])
       # print(row_display)
