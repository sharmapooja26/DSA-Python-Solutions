def is_sorted(arr):
    for i in range (len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        return True


arr = [2,4,5,2,5]
print("array is sorted:", is_sorted(arr))