def longestSubstring(s):
	start = maxlength =0
	dic = {}
	for i in range(len(s)):
		if s[i] in dic and start <= dic[s[i]]:
			start = dic[s[i]]+1
		else:
			maxlength = max(maxlength,i-start+1)

		dic[s[i]] = i

	return maxlength


s = "tmmzuxt"

print(longestSubstring(s))