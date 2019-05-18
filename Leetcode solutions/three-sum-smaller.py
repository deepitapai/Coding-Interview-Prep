def threeSumSmaller(nums,target):
	nums.sort()
	result = 0
	for i in range(len(nums)-2):
		l,r = i+1,len(nums)-1
		while l<r:
			total = nums[i]+nums[l]+nums[r]
			if total<target:
				result += r-l
				l +=1
			else:
				r -=1


	return result



print(threeSumSmaller([-2,0,1,3],2))