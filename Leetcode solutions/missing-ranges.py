def missingRanges(nums,lower,upper):
	res = []
	i=0
	nums.insert(0,lower-1)
	nums.append(upper+1)
	print(nums)
	while i<len(nums)-1:
		left,right = nums[i],nums[i+1]
		if left != right-1:
			if right-left == 2:
				res.append(str(right-1))

			elif right-left >2:
				print(left,right)
				res.append(str(left+1)+"->"+str(right-1))
		i +=1
	return res


nums = [1,1,1]
print(missingRanges(nums,1,1))