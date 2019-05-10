def firstMissingPositive(arr):
	if 1 not in arr:
		return 1

	for i in range(len(arr)):
		if arr[i] <=0 or arr[i]>len(arr):
			arr[i] = 1

	for i in range(len(arr)):
		idx = abs(arr[i])
		if arr[idx%len(arr)] <0: continue
		else:
			arr[idx%len(arr)] = -arr[idx%len(arr)]

	for i in range(1,len(arr)):
		if arr[i] >0:
			return i

	if arr[0] >0:
		return len(arr)


	return len(arr)+1


arr = [1,2,0]
print(firstMissingPositive(arr))

