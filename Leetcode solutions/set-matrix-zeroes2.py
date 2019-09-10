def setMatrixZeroes(matrix):
	is_col = False
	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			is_col = False
			break

	for i in range(len(matrix)):
		for j in range(1,len(matrix[0])):
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0

	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[0])):
			if matrix[i][0] == 0 or matrix[0][j] == 0:
				matrix[i][j] = 0

	if matrix[0][0] == 0:
		for j in range(len(matrix[0])):
			matrix[0][j] = 0

	if is_col:
		for i in range(len(matrix)):
			matrix[i][0] = 0


	return matrix

print(setMatrixZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]]))
