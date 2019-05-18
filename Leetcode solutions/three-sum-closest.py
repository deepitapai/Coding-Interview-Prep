def threeSumClosest(nums,target):
	nums.sort()
	mindiff = float('inf')
	for i in range(len(nums)-2):
		l,r = i+1,len(nums)-1
		while l<r:
			total = nums[i]+nums[l]+nums[r]
			diff = abs(target-total)
			if diff <mindiff:
				mindiff = diff
				sol = total

			if total<target:
				l +=1
			else:
				r -=1

	return sol


print(threeSumClosest([-4,-1,1,2],1))