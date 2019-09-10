def rotateImage(matrix):
	def clockwise(i,j):
		return j,n-i-1
	n = len(matrix)
	for i in range(n):
		for j in range(i,n-i-1):
			up_val = matrix[i][j]
			i_right,j_right = clockwise(i,j)
			i_bottom,j_bottom = clockwise(i_right,j_right)
			i_left,j_left = clockwise(i_bottom,j_bottom)

			matrix[i][j] = matrix[i_left][j_left]
			matrix[i_left][j_left] = matrix[i_bottom][j_bottom]
			matrix[i_bottom][j_bottom] = matrix[i_right][j_right]
			matrix[i_right][j_right] = up_val

	return matrix

print(rotateImage([
  [1,2,3],
  [4,5,6],
  [7,8,9]]))