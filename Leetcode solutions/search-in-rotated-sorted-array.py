def searchRotatedSortedArray(nums,target):
	l,h = 0,len(nums)-1
	while l<=h:
		mid = (l+h)//2
		# comparator = nums[mid]
		if (nums[mid] >= nums[0] and target>= nums[0]) or (nums[mid]<nums[0] and target <nums[0]):
			comparator = nums[mid]

		else:
			if target < nums[0]:
				comparator = float('-inf')
			elif target>nums[0]:
				comparator = float('inf')

		if comparator == target:
			return mid

		elif comparator<target:
			l = mid+1
		else:
			h = mid-1

	return -1

print(searchRotatedSortedArray([4,5,6,7,0,1,2],0))
