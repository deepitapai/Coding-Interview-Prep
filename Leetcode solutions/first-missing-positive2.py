def firstMissingPositive(nums):
	for i in range(len(nums)):
		if 0<nums[i]<len(nums) and nums[i] != nums[nums[i]-1]:
			nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]

	for i in range(len(nums)):
		if nums[i] != i+1:
			return i+1
	return len(nums)+1


print(firstMissingPositive([-1,3,4,1]))