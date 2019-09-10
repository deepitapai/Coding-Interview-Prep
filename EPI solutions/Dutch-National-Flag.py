# when order is important. Same as LC 75
def dutchNationalFlag(pivot_index,arr):
	pivot = arr[pivot_index]
	smaller,equal,larger = 0,0,len(arr)-1
	while equal<=larger:
		if arr[equal] < pivot:
			arr[equal],arr[smaller] = arr[smaller],arr[equal]
			smaller +=1
			equal +=1
		elif arr[equal] == pivot:
			equal +=1
		else:
			arr[equal],arr[larger] = arr[larger],arr[equal]
			larger -=1

	return arr

print(dutchNationalFlag(1,[0,1,2,2,0,1,0,2]))

# when order IS NOT important.
def dutchNationalFlagUnordered(pivot_index,arr):
	pivot = arr[pivot_index]
	smaller = 0
	for i in range(len(arr)):
		if arr[i] < pivot:
			arr[i],arr[smaller] = arr[smaller],arr[i]
			smaller +=1

	return arr

print(dutchNationalFlagUnordered(1,[0,1,2,2,0,1,0,2]))

# Variant: Order all False elements before True
def dutchNationalFlagVariant(arr):
	pivot = False
	dic = {False:0,True:1}
	smaller = 0
	for i in range(len(arr)):
		if dic[arr[i]] <= dic[pivot]:
			arr[i],arr[smaller] = arr[smaller],arr[i]
			smaller +=1

	return arr

print(dutchNationalFlagVariant([False,True,False,True,True,False,False]))