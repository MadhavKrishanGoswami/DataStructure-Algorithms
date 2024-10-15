def sort(arr, low, high):
    if(low >= high):
        return
    partition = sortfn(arr,low,high)
    sort(arr, low, partition-1)
    sort(arr, partition+1, high)
def sortfn(arr, low,high):
    pivot = arr[high]
    i = low
    j = high
    while i < j:
        while arr[i] < pivot:
            i+=1
        while arr[j] > pivot:
            j-=1
        if(i< j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1
    return j
arr = [5,4,3,2,1]
print(arr)
sort(arr, 0, len(arr)-1)
print(arr)
