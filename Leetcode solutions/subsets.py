def subsets(nums):
	result = []
	def dfs(nums,index,path,result):
		result.append(path)
		for i in range(index,len(nums)):
			dfs(nums,i+1,path+[nums[i]],result)

	dfs(sorted(nums),0,[],result)
	return result

print(subsets([1,2,3]))