def wildcardMatching(s,p):
	dp = [[False for f in range(len(p)+1)] for i in range(len(s)+1)]
	for i in range(1,len(p)+1):
		if p[i-1] != '*':
			break
		dp[0][i] = True

	dp[0][0] = True

	for i in range(1,len(dp[0])):
		for j in range(1,len(dp)):
			if p[i-1] == s[j-1] or p[i-1] == '?':
				dp[j][i] = dp[j-1][i-1]
			elif p[i-1] == '*':
				dp[j][i] = dp[j-1][i] or dp[j][i-1]

	return dp[-1][-1]

print(wildcardMatching('','*'))