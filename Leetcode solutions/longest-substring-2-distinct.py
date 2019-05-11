#uses sliding window approach
def twoMostDistinct(string):
	hashmap = {}
	left = 0
	right = 0
	n = len(string)
	maxlen = 0
	while right<n:
		if len(hashmap) < 3:
			hashmap[string[right]] = right
			right +=1

		if len(hashmap) == 3:
			idx = min(hashmap.values())
			del hashmap[string[idx]]
			left = idx+1

		maxlen = max(maxlen,right-left)

	return maxlen


string="aa"
print(twoMostDistinct(string))