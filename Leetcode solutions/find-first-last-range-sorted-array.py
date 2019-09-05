def searchRange(nums,target):
	def searchRangeLeft(nums,target):
		l,h = 0,len(nums)-1
		while l<=h:
			mid = (l+h)//2
			if nums[mid] < target:
				l = mid+1
			else:
				h = mid -1
		return l
	def searchRangeRight(nums,target):
		l,h = 0,len(nums)-1
		while l<=h:
			mid = (l+h)//2
			if nums[mid] <= target:
				l = mid+1
			else:
				h = mid -1
		return h

	left,right = searchRangeLeft(nums,target),searchRangeRight(nums,target)
	return (left,right) if left<=right else (-1,-1)


print(searchRange([5,7,7,8,8,10],8))
