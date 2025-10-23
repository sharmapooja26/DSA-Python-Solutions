def leftRotateByOne(arr):
    if len(arr) == 0:
        return arr
    first = arr[0]  
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first

    return arr


arr = [1, 2, 3, 4, 5]
print(leftRotateByOne(arr))  
