def merge(nums1,nums2,m,n):
	l1,l2,end = m-1,n-1,m+n-1
	while l1>=0 and l2>=0:
		if nums2[l2] >= nums1[l1]:
			nums1[end] = nums2[l2]
			l2 -=1
		else:
			nums1[end] = nums1[l1]
			l1 -=1

		end -=1

	if l1 <0:
		nums1[:l2+1] = nums2[:l2+1]

	return nums1

print(merge([7,8,9,0,0,0],[1,2,3],3,3))