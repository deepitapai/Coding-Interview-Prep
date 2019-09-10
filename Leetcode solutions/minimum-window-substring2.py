# https://leetcode.com/articles/minimum-window-substring/ -- APPROACH 1
from collections import Counter
def minimumWindowSubstring(s,t):
	dic_t = Counter(t)
	window_t = {}
	l,r = 0,0
	required = len(dic_t)
	formed = 0
	ans = float('inf'),None,None
	while r<len(s):
		char = s[r]
		window_t[char] = window_t.get(char,0)+1
		if window_t[char] == dic_t[char]:
			formed +=1
		while l<=r and formed == required:
			char = s[l]
			if r-l+1 < ans[0]:
				ans = (r-l+1,l,r)
			window_t[char] -=1
			if char in dic_t and window_t[char] < dic_t[char]:
				 formed -=1
			l +=1
		r +=1

	return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


print(minimumWindowSubstring('ADOBECODEBANC','ABC'))