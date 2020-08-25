# source : https://leetcode.com/problems/valid-sudoku/submissions/

"""
Runtime: 116 ms, faster than 50.32% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.6 MB, less than 99.09% of Python3 online submissions for Valid Sudoku.
"""
#def isValidSudoku(self, board: List[List[str]]) -> bool:
def isValidSudoku(board):
    #rows = len(board[0])
    #cols = len(board)
    # always 9

    
    return rowCheck(board) and colCheck(board) and gridCheck(board)

def gridCheck(board):
    for i in range(0,9,3):
        for j in range(0, 9,3):
            stringSol = ""
            for k in range(i,i+3):
                for l in range(j, j+3):
                    # k l to go over a grid
                    if (board[k][l]!= '.'):
                        if (stringSol.find(board[k][l]) != -1 ):
                            #print(stringSol.find(board[i][j]))
                            #print(k,l, board[k][l])
                            return False
                        else:
                            stringSol += board[k][l]

    return True
    

def rowCheck(board,istart=0, jstart=0, offset=9):
    #print(istart, jstart, offset)
    for i in range(istart, istart + offset):
            stringSol = ""
            for j in range(jstart, jstart + offset):
                if (board[i][j]!= '.'):
                    if (stringSol.find(board[i][j]) != -1 ):
                        #print(stringSol.find(board[i][j]))
                        #print(i,j, board[i][j])
                        return False
                    else:
                        stringSol += board[i][j]
    return True

def colCheck(board,istart=0, jstart=0, offset=9):
    #print(istart, jstart, offset)
    for i in range(istart, istart + offset):
            stringSol = ""
            for j in range(jstart, jstart + offset):
                if (board[j][i]!= '.'):

                    if (stringSol.find(board[j][i]) != -1 ):
                        #print(stringSol.find(board[j][i]))
                        #print(i,j, board[j][i])
                        return False
                    else:
                        stringSol += board[j][i]
                
    return True
        
        
        
"""
        
Input = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".",".",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]


print(isValidSudoku(Input))

"""