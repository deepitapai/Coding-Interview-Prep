def validSudoku(board):
	def isUnitValid(unit):
		unit = [i for i in unit if i!='.']
		return len(set(unit)) == len(unit)

	def checkRow(board):
		for row in board:
			if not isUnitValid(row):
				return False
		return True

	def checkCol(board):
		for col in zip(*board):
			if not isUnitValid(col):
				return False
		return True

	def checkBox(board):
		for i in range(0,7,3):
			for j in range(0,7,3):
				square = [board[k][l] for k in range(i,i+3) for l in range(j,j+3)]
				if not isUnitValid(square):
					return False
		return True

	return checkRow(board) and checkCol(board) and checkBox(board)

print(validSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]v))