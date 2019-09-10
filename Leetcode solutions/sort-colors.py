def sortColors(arr):
	red,white,blue = 0,0,len(arr)-1
	while white<=blue:
		if arr[white] == 0:
			arr[white],arr[red] = arr[red],arr[white]
			red +=1
			white +=1

		elif arr[white] == 1:
			white +=1

		else:
			arr[white],arr[blue] = arr[blue],arr[white]
			blue -=1

	return arr

print(sortColors([0,1,2,2,0,1,0,2]))