input = [0,0,1,1,1,2,2,3,3,4]
# output = 5
def removeDuplicates(nums):
    firstPointer = 1 
    for secondPointer in range(1, len(nums)):
        if nums[secondPointer] != nums[secondPointer -1]:
            nums[firstPointer] = nums[secondPointer]
            firstPointer += 1
    return firstPointer
print(removeDuplicates(input))