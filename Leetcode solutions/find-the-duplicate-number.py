#O(n) time, constant space, modified input using same approach as first missing positive number
def findDuplicate(arr):
	ele = 0
	while True:
		ele = arr[abs(ele)]
		if arr[abs(ele)] <0:
			return abs(ele)
		else:
			arr[abs(ele)]= -arr[abs(ele)]

arr = [1,4,6,6,6,2,3]
print(findDuplicate(arr))


#O(n) time, constant space, no modification
def findDuplicate1(arr):
	short_ptr = arr[0]
	fast_ptr = arr[0]
	while True:
		short_ptr= arr[short_ptr]
		fast_ptr = arr[arr[fast_ptr]]
		if short_ptr == fast_ptr:
			break

	ptr_1 = arr[0]
	ptr_2 = short_ptr

	while ptr_1 != ptr_2:
		ptr_1 = arr[ptr_1]
		ptr_2 = arr[ptr_2]

	return ptr_1

arr = [1,4,6,6,6,2,3]
print(findDuplicate1(arr))