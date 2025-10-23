def LargestElement(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val 


arr = [2,4,6,8,1]
print("largest element is:" ,LargestElement(arr))