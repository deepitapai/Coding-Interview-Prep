def decodeWays(s):
	dp = [0]*(len(s)+1)
	dp[0] = 1
	for i in range(1,len(s)+1):
		if s[i-1] != '0':
			dp[i] += dp[i-1]
		if len(s[i-2:i]) >=2 and '10' <= s[i-2:i] <= '26':
			dp[i] += dp[i-2]

	return dp[len(s)]

print(decodeWays('226'))