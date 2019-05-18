#BRUTE FORCE
def trappingRainWater(nums):
	ans = 0
	max_left = nums[0]
	max_right = 0
	for i in range(1,len(nums)-1):
		max_left = nums[0]
		max_right = 0
		for j in range(i+1):
			max_left = max(max_left,nums[j])
		print("max_left",max_left)
		for j in range(len(nums)-1,i-1,-1):
			max_right = max(max_right,nums[j])
		print("max_right",max_right)
		print("num:",nums[i])
		ans +=min(max_left,max_right)-nums[i]
		print(ans)

	return ans

def trappingRainWaterDP(nums):
	max_left = [0]*len(nums)
	max_left[0] = nums[0]
	ans = 0
	max_right = [0]*len(nums)
	for i in range(1,len(nums)-1):
		# print(max_left[i-1])
		# print(nums[i])
		max_left[i] = max(max_left[i-1],nums[i])
	max_right[len(nums)-1] = nums[len(nums)-1]
	for i in range(len(nums)-2,-1,-1):
		max_right[i] = max(max_right[i+1],nums[i])
	for i in range(1,len(nums)-1):
		ans += min(max_left[i],max_right[i])-nums[i]

	return ans
print(trappingRainWaterDP([0,1,0,2,1,0,1,3,2,1,2,1]))