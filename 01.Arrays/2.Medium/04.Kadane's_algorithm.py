# QUESTION:-
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1: Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6 (subarray [4,-1,2,1])
# Example 2: Input: nums = [1], Output: 1

# APPROACH:-
# Use Kadane's Algorithm
# Initialize curr_sum = 0, ans = INT_MIN
# For each element:
#   Add element to curr_sum
#   Update ans = max(ans, curr_sum)
#   If curr_sum < 0, reset to 0
# Return ans

# CODE:-
def maxSubArray(nums):
    """Find the maximum sum of any contiguous subarray"""
    curr_sum = 0
    ans = float('-inf')
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        ans = max(ans, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    
    return ans


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = maxSubArray(nums1)
    print(f"Output: {result1}")
    print("Expected: 6")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [1]
    result2 = maxSubArray(nums2)
    print(f"Output: {result2}")
    print("Expected: 1")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
