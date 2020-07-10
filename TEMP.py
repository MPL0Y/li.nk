if __debug__:
	import sys
	sys.stdin = open('inputpy.txt', 'r')
	sys.stdout = open('outputpy.txt', 'w')

def partition(arr, l, h): 
	i = l - 1
	pivot = arr[h]
	for j in range(l, h):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i] 
	arr[i+1], arr[h] = arr[h], arr[i+1] 
	return i + 1

def quick_sort(arr, l, h): 
	if l < h:
		pi = partition(arr, l, h)
		quick_sort(arr, l, pi-1)
		quick_sort(arr, pi+1, h)

l = list(map(int, input().split()))
quick_sort(l, 0, len(l)-1)
print(*l)