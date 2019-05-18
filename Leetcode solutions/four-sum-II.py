def fourSumII(A,B,C,D):
	d = {}
	for i in range(len(A)):
		for j in range(len(A)):
			total = A[i]+B[j]
			if total not in d:
				d[total] = 1
			else:
				d[total] +=1
	result =0
	for i in range(len(A)):
		for j in range(len(A)):
			if -(C[i]+D[j]) in d:
				result += d[-(C[i]+D[j])]

	return result

print(fourSumII([1,2],[-2,-1],[-1,2],[0,2]))