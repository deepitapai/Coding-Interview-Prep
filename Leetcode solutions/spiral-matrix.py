def spiralMatrix(matrix):
	result = []
	if not matrix:
		return result
	u,d,l,r = 0,len(matrix)-1,0,len(matrix[0])-1

	while u<d and l<r:
		result.extend([matrix[u][i] for i in range(l,r)])
		result.extend([matrix[i][r] for i in range(u,d)])
		result.extend([matrix[d][i] for i in range(r,l,-1)])

		u,d,l,r = u+1,d-1,l+1,r-1

	if u == d:
		result.extend([matrix[u][i] for i in range(l,r)])
	elif l == r:
		result.extend([matrix[i][l] for i in range(u,d+1)])

	return result

matrix = [[2],[3]]
print(spiralMatrix(matrix))