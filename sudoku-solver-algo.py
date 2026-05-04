import numpy as np

sudoku_grid = [
            [0,0,8,0,0,0,0,1,6],
            [5,0,0,0,9,2,0,0,8],
            [0,0,0,1,0,0,0,0,0],
            [9,0,0,3,0,0,8,2,0],
            [0,2,0,0,0,0,0,7,0],
            [0,8,4,0,0,6,0,0,5],
            [0,0,0,0,0,3,0,0,0],
            [4,0,0,9,6,0,0,0,2],
            [1,6,0,0,0,0,7,0,0]
]


def is_valid(row_index, column_index, number):
    global sudoku_grid
    
    for n in range(0,9):
        # Check if the row already has that number
        if sudoku_grid[row_index][n] == number:
            return False
    
    for n in range(0,9):
        # Now check the column
        if sudoku_grid[n][column_index] == number:
            return False

    # To index each of the 3x3 squares, we divide two numbers and return the whole number
    # The first 3x3 square is indexed as 0, then 1, then 3
    square_col = (column_index // 3) * 3
    square_row = (row_index // 3) * 3

    for n in range(0,3):
        for m in range(0,3):
            #  Check if the square already has the number
            if sudoku_grid[square_row+n][square_col+m] == number:
                return False
    return True

def solve():
    global sudoku_grid
    
    for row in range(0,9):
        for column in range(0,9):
            # Check if blank
            if sudoku_grid[row][column] == 0:
                for number in(range(1,10)):
                    # Check if valid
                    if is_valid(row, column, number):
                        sudoku_grid[row][column] = number
                        solve()
                        
                        # If we've made the wrong guess, set the spaceback to 0 and return the for loop
                        sudoku_grid[row][column] = 0
                return           
    print(np.matrix(sudoku_grid))
    input('Press enter for more solutions.')
    return
                
solve()