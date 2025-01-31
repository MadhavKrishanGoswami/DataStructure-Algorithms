
# Online Python - IDE, Editor, Compiler, Interpreter

def BinarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left + right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

array = [2,5,7,8]
print(BinarySearch(array,8))