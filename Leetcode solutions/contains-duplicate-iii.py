# Using buckets: Linear
def containsDuplicateIII(nums,k,t):
	if t < 0:
		return False
	cache = {}
	for i in range(0,len(nums)):
		if i-k>0:
			delete_bucket_id = nums[i-k-1]//(t+1)
			del cache[delete_bucket_id]
		bucket_id = nums[i]//(t+1)
		condition1 = (bucket_id in cache)
		condition2 = (bucket_id-1 in cache and abs(cache[bucket_id-1]-nums[i]) <=t)
		condition3 = (bucket_id+1 in cache and abs(cache[bucket_id+1]-nums[i]) <=t)
		if condition1 or condition2 or condition3:
			return True

		cache[bucket_id] = nums[i]
	return False

# Brute force: O(n*k)
def containsDuplicateIII2(nums,k,t):
	for i in range(0,len(nums)):
		for j in range(i+1,i+k+1):
			if j < len(nums):
				if abs(nums[i]-nums[j]) <= t:
					return True
	return False

print(containsDuplicateIII([1,5,9,1,5,9],2,3))
print(containsDuplicateIII2([1,2,3,1],3,0))