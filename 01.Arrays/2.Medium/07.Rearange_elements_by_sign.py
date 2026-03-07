"""
QUESTION:-
You are given a 0-indexed integer array nums of even length consisting of an equal number 
of positive and negative integers.
You should rearrange the elements of nums such that the modified array follows the given conditions:
- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in nums is preserved.
- The rearranged array begins with a positive integer.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
"""

# APPROACH:-
# Use two pointers: one for positive integers (even indices) and one for negative integers (odd indices).
# Iterate through the array and place positive numbers at even positions and negative numbers at odd positions.

# CODE:-

def rearrangeArray(nums):
    """
    Rearrange array to have alternating positive and negative numbers.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(nums)
    ans = [0] * n
    pos_idx = 0  # for positive integers (even indices)
    neg_idx = 1  # for negative integers (odd indices)
    
    for num in nums:
        if num >= 0:
            ans[pos_idx] = num
            pos_idx += 2
        else:
            ans[neg_idx] = num
            neg_idx += 2
    
    return ans


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    nums1 = [3, 1, -2, -5, 2, -4]
    result1 = rearrangeArray(nums1)
    print(f"Input: nums = {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [3,-2,1,-5,2,-4]")
    print()

    # Test case 2
    print("Test 2:")
    nums2 = [1, 2, -4, -5]
    result2 = rearrangeArray(nums2)
    print(f"Input: nums = {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [1,-4,2,-5]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)