def containerMostWater(arr):
	maxArea = 0
	l,r = 0,len(arr)-1
	while l<r:
		maxArea = max(maxArea,min(arr[l],arr[r])*(r-l))
		if arr[l] <= arr[r]:
			l +=1
		else:
			r -=1

	return maxArea

print(containerMostWater([1,8,6,2,5,4,8,3,7]))