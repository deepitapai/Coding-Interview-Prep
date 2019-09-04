# Linear time, constant space
def jumpGame(arr):
	max_reach,n=0,len(arr)
	for i,x in enumerate(arr):
		if max_reach<i:
			return False
		if max_reach>=n-1:
			return True
		max_reach = max(max_reach,i+x)


arr = [1,2,4]
print(jumpGame(arr))
