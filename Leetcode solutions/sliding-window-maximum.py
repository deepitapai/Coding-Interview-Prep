from collections import deque
def slidingWindowMax(nums,k):
	deq,output = deque(),[]
	n = len(nums)
	def clean_deq(deq,i):
		while deq and deq[0] == i-k:
			deq.popleft()
		while deq and nums[deq[-1]] < nums[i]:
			deq.pop()

	for i in range(k):
		clean_deq(deq,i)
		deq.append(i)
	output.append(nums[deq[0]])

	for i in range(k,n):
		clean_deq(deq,i)
		deq.append(i)
		output.append(nums[deq[0]])

	return output
	
print(slidingWindowMax([1,3,-1,-3,5,3,6,7],3))
