#!/usr/bin/python
from numpy import rot90

def sudoku(puzzle):
    # 405 is the grand total sum of the puzzle
    while sum([sum(row) for row in puzzle]) != 405:
        # reset these for each iteration otherwise older "missing values" persist
        row_missing_values = [[] for x in range(9)]
        col_missing_values = [[] for x in range(9)]
        
        # find the missing values for each row
        for r,row in enumerate(puzzle):
            for n in range(1,10):
                if n not in row:
                    row_missing_values[r].append(n)
        
        # rotate to check the columns because I'm lazy and don't wanna do the math for
        # getting all the missing values of the columns otherwise
        puzzle = rot90(puzzle,-1)
        
        # find the missing values for each column
        for c,col in enumerate(puzzle):
            for n in range(1,10):
                if n not in col:
                    col_missing_values[c].append(n)
                    
        # reset the rotation
        puzzle = rot90(puzzle)
        
        # get the missing values for the regions (the 3x3 grids)
        nw_missing_values = [n for n in range(1,10) if n not in puzzle[0][0:3] and n not in puzzle[1][0:3] and n not in puzzle[2][0:3]]
        nn_missing_values = [n for n in range(1,10) if n not in puzzle[0][3:6] and n not in puzzle[1][3:6] and n not in puzzle[2][3:6]]
        ne_missing_values = [n for n in range(1,10) if n not in puzzle[0][6:9] and n not in puzzle[1][6:9] and n not in puzzle[2][6:9]]
        ww_missing_values = [n for n in range(1,10) if n not in puzzle[3][0:3] and n not in puzzle[4][0:3] and n not in puzzle[5][0:3]]
        cc_missing_values = [n for n in range(1,10) if n not in puzzle[3][3:6] and n not in puzzle[4][3:6] and n not in puzzle[5][3:6]]
        ee_missing_values = [n for n in range(1,10) if n not in puzzle[3][6:9] and n not in puzzle[4][6:9] and n not in puzzle[5][6:9]]
        se_missing_values = [n for n in range(1,10) if n not in puzzle[6][0:3] and n not in puzzle[7][0:3] and n not in puzzle[8][0:3]]
        ss_missing_values = [n for n in range(1,10) if n not in puzzle[6][3:6] and n not in puzzle[7][3:6] and n not in puzzle[8][3:6]]
        sw_missing_values = [n for n in range(1,10) if n not in puzzle[6][6:9] and n not in puzzle[7][6:9] and n not in puzzle[8][6:9]]
        
        # put them in a 3x3 grid for ease of access later
        region_missing_values = [
            [nw_missing_values,nn_missing_values,ne_missing_values],
            [ww_missing_values,cc_missing_values,ee_missing_values],
            [se_missing_values,ss_missing_values,sw_missing_values]
        ]
        
        # getting each cell's missing values
        for r,row in enumerate(puzzle):
            for c,col in enumerate(row):
                # only run if the value of the cell is missing
                if puzzle[r][c] == 0:
                    
                    # generate the list of each cell's missing values 
                    # by only grabbing the shared digits between the 
                    # associated row, column, and region
                    valid_numbers_for_cell = [n for n in range(1,10) if n in row_missing_values[r] and n in col_missing_values[c] and n in region_missing_values[int(r/3)][int(c/3)]]
                    
                    # if it only has 1 shared value between the 3 lists,
                    # that value is the only number that cell can be!
                    if len(valid_numbers_for_cell) == 1:
                        puzzle[r][c] = valid_numbers_for_cell[0]
                    
    return puzzle.tolist()

if __name__ == "__main__":
    print("reading from file or input is a work in progress")