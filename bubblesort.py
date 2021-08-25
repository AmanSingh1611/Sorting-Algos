def bubblesort(arr):
	indexing_length=len(arr)-1
	Sorted = False
	while not Sorted :
		Sorted=True
		for i in range(indexing_length):
			if arr[i]>arr[i+1]:
				Sorted=False
				arr[i],arr[i+1]=arr[i+1],arr[i]
	return arr
arr =list(map(int,input().split()))
print(bubblesort(arr))				

