def permutations(nums):
	result = []
	visited = set()
	def backtracking(nums,result,visited,subset):
		if len(subset) == len(nums):
			result.append(subset)
			return

		for i in range(len(nums)):
			if i not in visited:
				visited.add(i)
				backtracking(nums,result,visited,subset+[nums[i]])
				visited.remove(i)

	backtracking(nums,result,visited,[])
	return result

print(permutations([1,2,3]))