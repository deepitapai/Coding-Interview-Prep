def longestPalindromicSubsequence(string):
	res = ""
	for i in range(len(string)):
		tmp = helper(string,i,i)
		if len(tmp) > len(res):
			res = tmp

		tmp = helper(string,i,i+1)
		if len(tmp) > len(res):
			res = tmp

	return res

def helper(s,l,r):
	while l>=0 and r<len(s) and s[l] == s[r]:
		l -=1
		r +=1

	return s[l+1:r]


string = "abbaba"

print(longestPalindromicSubsequence(string))