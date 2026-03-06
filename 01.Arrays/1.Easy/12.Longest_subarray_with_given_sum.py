# QUESTION:-
# You are given an array 'A' of size 'N' and an integer 'K'.
# Find the length of longest subarray with sum = K
# Example: Input: [1,2,3,1,1,1,1], K=3, Output: 3 (subarray [3] or [1,1,1])

# APPROACH:-
# Use sliding window technique with two pointers (start and end)
# Maintain a sum of current window
# If sum equals k, update max length
# If sum exceeds k, remove elements from start
# Continue until end of array

# CODE:-
def longestSubarrayWithSumK(a, k):
    """Find the length of longest subarray with given sum k"""
    start = 0
    ans = 0
    total_sum = 0
    n = len(a)
    
    for end in range(n):
        total_sum += a[end]
        while total_sum > k:
            total_sum -= a[start]
            start += 1
        if total_sum == k:
            ans = max(ans, end - start + 1)
    
    return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 1, 1, 1, 1]
    k = 3
    result = longestSubarrayWithSumK(arr, k)
    print(f"Output: {result}")
    print("Expected: 3")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
