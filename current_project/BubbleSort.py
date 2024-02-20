def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        print("i {}".format(i))
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)

arr = [5, 2, 8, 12, 3]
print(bubble_sort(arr))


