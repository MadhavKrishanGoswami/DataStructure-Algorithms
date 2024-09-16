def mergesort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    leftSide = arr[:mid]
    rightSide = arr[mid:]
    leftSide = mergesort(leftSide)
    rightSide = mergesort(rightSide)
    return merge(leftSide, rightSide)
def merge(left,right):
    new = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

array = [5,4,3]

print(mergesort(array))
