# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
def threesum(arr):
	arr = sorted(arr)
	i=0
	result = []
	for i in range(len(arr)-2):
		if arr[i] >0:
			break
		if i>0 and arr[i] == arr[i-1]:
			continue
		l,r = i+1,len(arr)-1

		while l<r:
			total = arr[i] + arr[l] + arr[r]
			if total <0:
				l +=1
			elif total >0:
				r -=1

			else:
				result.append([arr[i],arr[l],arr[r]])
				while l<r and arr[l] == arr[l+1]:
					l +=1
				while l<r and arr[r] == arr[r-1]:
					r -=1

				l +=1
				r -=1
	return result


lst = [0,0,0]
print(threesum(lst))
