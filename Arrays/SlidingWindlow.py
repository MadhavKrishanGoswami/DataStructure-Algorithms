Input = [2, 1, 5, 1, 3, 2]
k = 3
#output = 9 
def maxSum(K, arr):
    window_sum = sum(arr[:K])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k] # sliding window
        max_sum = max(max_sum, window_sum) # max sum
    return max_sum

print(maxSum(k, Input))
# Time complexity: O(N)