def productExceptSelf(arr):
	output = []
	p = 1
	for i in range(len(arr)):
		output.append(p)
		p = p*arr[i]

	p =1
	for i in range(len(arr)-1,-1,-1):
		output[i] = output[i]*p
		p = p*arr[i]

	return output


output = [1,2,3,4]
print(productExceptSelf(output))