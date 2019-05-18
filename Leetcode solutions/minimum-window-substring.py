from collections import Counter
def minWindowSubstring(string,target):
	l,r = 0,0
	dict_t = Counter(target)
	required = len(dict_t)
	formed = 0
	window_count = dict()
	ans = float('inf'),None,None
	while r< len(string):
		char = string[r]
		window_count[char] = window_count.get(char,0)+1
		if char in dict_t and window_count[char] == dict_t[char]:
			formed +=1

		while l<=r and formed == required:
			char = string[l]
			window_count[char] -=1
			if r-l+1 < ans[0]:
				ans = r-l+1,l,r

			if char in dict_t and window_count[char] < dict_t[char]:
				formed -=1

			l +=1

		r +=1

	return string[ans[1]:ans[2]]



print(minWindowSubstring("ADOBECODEBANC","ABC"))
