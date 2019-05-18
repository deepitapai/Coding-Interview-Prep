def twoSum(nums,target):
	d = {}
	for i in range(len(nums)):
		if target-nums[i] in d and d[target-nums[i]] !=i:
			return(d[target-nums[i]],i)

		d[nums[i]] = i

nums = [2,7,11,15]
print(twoSum(nums,9))