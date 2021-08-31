def heapify(arr, n, i):
    grande = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[grande] < arr[l]:
        grande = l
    if r < n and arr[grande] < arr[r]:
        grande = r
    if grande != i:
        arr[i], arr[grande] = arr[grande], arr[i]
        heapify(arr, n, grande) 
def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
arr = [2,40,7,21,34,12,42,76]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])