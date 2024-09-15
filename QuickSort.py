
# Online Python - IDE, Editor, Compiler, Interpreter

def quicksort(arr):
    quicksortfn(arr,0,len(arr)-1)
    
def quicksortfn(arr, left, right):
    if left<right:
        partition_pos= partitionnsort(arr, left, right)
        quicksortfn(arr, left,partition_pos-1)
        quicksortfn(arr, partition_pos+1,right)

def partitionnsort(arr, left, right):
    i = left
    j = right-1
    pivot = arr[right]
    while i<j:
        while arr[i]< pivot and i<right:
            i+=1 
        while arr[j]> pivot and j>left:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i;

arr =[9,8,7,6,5,4,3,2,1]
quicksort(arr)
print(arr)