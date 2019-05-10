
# arr = [10,7,-1,0,1,3,4,5,6,7]

def bruteforcesolution(arr):
	current_streak = 0
	current_num = arr[0]
	longest_streak = 0
	for i in range(len(arr)):
		current_num = arr[i]
		current_streak = 1
		while current_num+1 in arr:
			current_num +=1
			current_streak +=1

		longest_streak = max(longest_streak,current_streak)

	return longest_streak

def sortedmethod(arr):
	sort_arr = sorted(arr)
	current_streak = 1
	longest_streak = 1
	for i in range(1,len(sort_arr)):
		if sort_arr[i] != sort_arr[i-1]:
			if sort_arr[i] == sort_arr[i-1]+1:
				current_streak +=1
			else:
				longest_streak = max(longest_streak,current_streak)				
				current_streak = 1

	return max(longest_streak,current_streak)




def longestContSubsequence(arr):
	current_streak = 0
	longest_streak = 0
	current_num = arr[0]
	set_arr = set(arr)
	# print(set_arr)
	for i in range(len(arr)):
		if arr[i]-1 not in set(arr):
			current_num = arr[i]
			# print(current_num)
			current_streak = 1

			while current_num+1 in set_arr:
				current_num +=1
				current_streak +=1

			longest_streak = max(longest_streak,current_streak)
	return longest_streak

# arr = [8,-1,0,1,3,-2,-5,4,5,6,7]
arr = [0,-1]
print(longestContSubsequence(arr))
