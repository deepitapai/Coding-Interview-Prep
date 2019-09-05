def mergeIntervals(intervals):
	intervals = sorted(intervals,key=lambda x:x[0])
	interval = intervals[0]
	result = []
	for i in range(1,len(intervals)):
		interval2 = intervals[i]
		if interval2[0]>interval[1]:
			result.append(interval)
			interval = interval2
		else:
			interval[1] = max(interval[1],interval2[1])

	result.append(interval)
	return result

print(mergeIntervals([[2,6],[1,3],[5,10]]))