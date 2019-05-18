def fourSum(nums,target):
	d = dict()
	for i in range(len(nums)):
		for j in range(i+1,len(nums)):
			s = nums[i]+nums[j]
			if s not in d:
				d[s] = [(i,j)]

			else:
				d[s].append((i,j))

	result = set()
	for key in d:
		value = target-key
		if value in d:
			list1 = d[key]
			list2 = d[value]
			for i,j in list1:
				for k,l in list2:
					if i!=k and i!=l and j!=k and j!=l:
						flist = [nums[i],nums[j],nums[k],nums[l]]
						flist.sort()
						result.add(tuple(flist))

	return list(result)


nums = [-2,-1,0,0,1,2]
print(fourSum(nums,0))