def BubbleSort(arr):
    n = len(arr) #6

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

arr = [64,34,25,12,11,90]

BubbleSort(arr)

print("Sorted data:")

for i in range(len(arr)):
    print("%d" % arr[i])