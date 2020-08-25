def isValidSudoku( board):
        width = len(board[0])
        height = len(board)
        
        for i in range(width + 1):
            stringSol = ""
            for j in range(height + 1):
                if (bool(stringSol.find(board[i][j])) and board[i][j]!= '.'):
                    return False
                else:
                    stringSol += board[i][j]
            return True

Input = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(Input))