def selection_sort(arr):
	for i in range(0,len(arr)-1):
		min_val = i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[min_val]:
				min_val=j
		if min_val!=i:
			arr[min_val],arr[i]=arr[i],arr[min_val]

arr=list(map(int,input().split()))
print(selection_sort(arr))