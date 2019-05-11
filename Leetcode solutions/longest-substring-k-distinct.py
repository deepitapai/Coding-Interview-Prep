from collections import OrderedDict
def kDistinct(string,k):
	hashmap = OrderedDict()
	left = 0
	right = 0
	maxlen = 0
	n = len(string)
	while right < n:
		if len(hashmap)<k+1:
			if string[right] in hashmap:
				del hashmap[string[right]]
			hashmap[string[right]] = right
			right +=1

		if len(hashmap) == k+1:
			val,idx = hashmap.popitems(last=False)
			del hashmap[string[idx]]
			left = idx+1

		maxlen = max(maxlen,right-left)

	return maxlen


print(kDistinct("eceba",4))