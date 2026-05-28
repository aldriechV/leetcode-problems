"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


def isValidSudoku(board):
        #check the boxes here
        
        #Col ranges: 0-3, 3-6, 6-9
        for i in range(0,3):
            for j in range(0,3):
                valid = {}
                for row in range(i*3,i*3+3): # column
                    for col in range(j*3,j*3+3): # rows
                        val = board[row][col]
                        print(val)
                        if val in valid and val != ".":
                            return False
                        else:
                            valid[val] = 1
            


        valid = {}
        for i in range(len(board)):
            #checks the cols
            valid = {}
            for j in range(len(board)):
                    if board[i][j] in valid and board[i][j] != ".":
                        return False
                    else:
                        valid[board[i][j]] = 1

            valid = {}
            #checks the rows
            for j in range(len(board)):
                if board[j][i] in valid and board[j][i] != ".":
                    return False
                else:
                    valid[board[j][i]] = 1
            valid = {}
            
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

isValidSudoku(board)
