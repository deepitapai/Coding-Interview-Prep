def setMatrixZeroes(matrix):
	zeroCol = False
	R = len(matrix)
	C = len(matrix[0])
	for i in range(R):
		if matrix[i][0] == 0:
			zeroCol = True
		for j in range(1,C):
			if matrix[i][j] == 0:
				print("i",i)
				print("j",j)
				matrix[i][0] = 0
				matrix[0][j] = 0
	print(matrix)
	for i in range(1,R):
		if matrix[i][0] == 0:
			for j in range(1,C):
				matrix[i][j] = 0

	for j in range(1,C):
		if matrix[0][j] == 0:
			for i in range(1,R):
				matrix[i][j] = 0

	if matrix[0][0] == 0:
		for j in range(C):
			matrix[0][j] = 0

	if zeroCol:
		for i in range(R):
			matrix[i][0] = 0


	return matrix


matrix = [[1,0,3]]

print(setMatrixZeroes(matrix))