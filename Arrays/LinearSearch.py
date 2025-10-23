def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    

print(LinearSearch([2,4,5,6,7],5))    