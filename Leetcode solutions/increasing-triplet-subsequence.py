def increasingTripletSubsequence(arr):
	minOne = float('inf')
	minTwo = float('inf')
	for i in range(len(arr)):
		if arr[i] < minOne:
			minOne = arr[i]
		if arr[i] > minOne:
			minTwo = min(minTwo,arr[i])
		if arr[i] > minTwo:
			return True

	return False


print(increasingTripletSubsequence([5,1,4,3,3,6]))