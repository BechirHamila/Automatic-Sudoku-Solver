grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0] ]





def verify_valid(grid,r,c,k):
    not_in_row= k not in grid[r]
    not_in_col=[k not in grid[i][c] for i in range(9)]
    not_in_square=[k not in grid [i][j] for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)]
    return not_in_row and not_in_col and not_in_square




