def wordAnagram(strs):
	dic = {}
	for i in sorted(strs):
		word = "".join(sorted(i))
		dic[word] = dic.get(word,[]) + [i]

	return list(dic.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(wordAnagram(strs))