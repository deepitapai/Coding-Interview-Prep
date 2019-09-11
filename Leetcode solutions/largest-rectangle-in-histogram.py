# if the next bar is greater than current, calculate area so far, else add index to stack
def largestRectangle(heights):
	heights.append(0)
	stack = [-1]
	ans = -1
	for i in range(len(heights)):
		while heights[i] < heights[stack[-1]]:
			h = heights[stack.pop()]
			w = i-stack[-1]-1
			ans = max(ans,w*h)
		stack.append(i)
	heights.pop()

	return ans if ans > -1 else 0

print(largestRectangle([2,1,5,6,2,3]))