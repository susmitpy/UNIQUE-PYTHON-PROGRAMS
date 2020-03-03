"""
A sudoku Solver.
Solves sudoku completes till Medium Difficulty.
After that human intelligence is needed.

"""

import numpy as np
""" Very Hard
s = np.array([
       [0, 0, 4, 0, 6, 0, 2, 0, 0],
       [0, 0, 0, 8, 0, 4, 0, 0, 0],
       [2, 0, 0, 0, 0, 0, 0, 0, 5],
       [0, 6, 0, 1, 0, 2, 0, 9, 0],
       [0, 8, 0, 6, 9, 5, 0, 3, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 7],
       [5, 9, 0, 0, 0, 0, 0, 4, 1],
       [0, 0, 0, 9, 0, 3, 0, 0, 0],
       [0, 0, 6, 0, 0, 0, 9, 0, 0]
       ])

       # Already: 26
       # Filled by program: 17

"""
"""Hard
s = np.array([
       [0, 6, 1, 3, 8, 0, 0, 0, 0],
       [7, 0, 0, 0, 0, 5, 0, 2, 0],
       [0, 0, 2, 0, 9, 0, 0, 0, 1],
       [0, 5, 9, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 4, 0, 8, 5, 0],
       [8, 0, 0, 0, 7, 0, 6, 0, 0],
       [0, 1, 0, 4, 0, 0, 0, 0, 9],
       [0, 0, 0, 0, 5 , 3, 4, 1, 0]
            ])
#Already: 26
#Filled by program: 27

"""

"""Medium """

s = np.array([
       [0, 0, 0, 4, 0, 0, 0, 7, 0],
       [6, 0, 0, 3, 5, 9, 0, 0, 0],
       [0, 0, 4, 0, 6, 0, 2, 0, 0],
       [0, 6, 0, 7, 0, 5, 0, 4, 1],
       [0, 3, 5, 0, 0, 0, 7, 2, 0],
       [4, 7, 0, 2, 0, 6, 0, 8, 0],
       [0, 0, 8, 0, 2, 0, 9, 0, 0],
       [0, 0, 0, 6, 7, 3, 0, 0, 4],
       [0, 4, 0, 0, 0, 8, 0, 0, 0]
            ])

# Already: 32
# Filled by program: 49


already = 0
for r in range(9):
    for c in range(9):
        if s[r,c] != 0:
            already+=1



def get_box_limits(r,c):
    r_min, r_max, c_min, c_max = None,None,None,None
    if r <= 2:
        r_min = 0
        r_max = 2
    elif r <= 5:
        r_min = 3
        r_max = 5
    else:
        r_min = 6
        r_max = 8
    if c <= 2:
        c_min = 0
        c_max = 2
    elif c <= 5:
        c_min = 3
        c_max = 5
    else:
        c_min = 6
        c_max = 8
    return {"ri":r_min,"ra":r_max,"ci":c_min,"ca":c_max}

def get_only_possible_row(row):
    occurence = dict()
    for i, j in enumerate(row):
        if type(j) == set:
                for k in j:
                    if k in occurence:
                        occurence[k] = False
                    else:
                        occurence[k] = (k,i)
    return occurence


def get_only_possible_col(col):
    occurence = dict()
    for i, j in enumerate(col):
        if type(j) == set:
                for k in j:
                    if k in occurence:
                        occurence[k] = False
                    else:
                        occurence[k] = (k,i)
    return occurence


def get_only_possible_box(box):
    """
        Given a box: 2D array where each element is a set containign possibilities
        return x,y coord along with the only possible no. at x,y
    """
    x=0
    y=0
    n=0
    occurence = {}
    for i in range(3):
        for j in range(3):
            if type(box[i,j]) == set:
                for k in box[i,j]:
                    if k in occurence:
                        occurence[k] = False
                    else:
                        occurence[k] = (i,j)
    for k,v in occurence.items():
        if type(v) != bool:
                return (v[0],v[1],k)
    return (3,3,3)

#sudoku = np.zeros((9,9),dtype=int)
possibilites = np.full((9,9),set([1,2,3,4,5,6,7,8,9]))
for i in range(30):
    for r in range(9):
        for c in range(9):
            if s[r][c] == 0:
                row_present = s[r,:]
                col_present = s[:,c]
                l = get_box_limits(r,c) # Box limits
                box = s[l["ri"]:l["ra"]+1,l["ci"]:l["ca"]+1]
                box_present = box.flatten()
                possibilites[r][c] = possibilites[r][c].difference(row_present.tolist()+col_present.tolist()+box_present.tolist())
            else:
                possibilites[r][c] = s[r][c]

    for r in range(0,9,3):
        for c in range(0,9,3):
            x,y,n = get_only_possible_box(possibilites[r:r+3,c:c+3])
            if x != 3:
                s[r+x][c+y] = n

    for r in range(9):
        row = possibilites[r,:]
        conf = get_only_possible_row(row)
        for k,v in conf.items():
            if type(v) !=bool:
                s[r,v[1]] = k

    for c in range(9):
        col = possibilites[:,c]
        conf = get_only_possible_col(col)
        for k,v in conf.items():
            if type(v) !=bool:
                s[v[1],c] = k


    for r in range(9):
        for c in range(9):
            if type(possibilites[r,c]) == set:
                if len(possibilites[r,c]) == 1:
                    s[r,c] = possibilites[r,c].pop()
filled = 0
for r in range(9):
    for c in range(9):
        if s[r,c] != 0:
            filled+=1

print(f"Already: {already}")
print(f"Filled by program: {filled-already}")

print(s)
