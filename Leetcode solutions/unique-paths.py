def uniquePaths(m,n):
	dp = [[1 for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]

	return dp[-1][-1]

print(uniquePaths(3,2))