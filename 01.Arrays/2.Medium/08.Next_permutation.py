"""
QUESTION:-
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

The next permutation of an array of integers is the next lexicographically greater permutation 
of its integer.

For example, the next permutation of arr = [1,2,3] is [1,3,2].
While the next permutation of arr = [3,2,1] is [1,2,3] (wraps around).

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
"""

# APPROACH:-
# 1. Find the first index i from right where nums[i] < nums[i+1] (break point)
# 2. If found, find the first index j from right where nums[j] > nums[i], swap them
# 3. Reverse the subarray from i+1 to end
# 4. If no break point found, reverse entire array

# CODE:-

def nextPermutation(nums):
    """
    Modify the array to contain the next lexicographically greater permutation.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # Find the break point (rightmost element where nums[i] < nums[i+1])
    break_point = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break_point = i
            break
    
    # If break point found, find element to swap with
    if break_point != -1:
        # Find rightmost element greater than nums[break_point]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[break_point]:
                # Swap
                nums[i], nums[break_point] = nums[break_point], nums[i]
                break
    
    # Reverse the array from break_point+1 to end
    nums[break_point + 1:] = reversed(nums[break_point + 1:])


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    nums1 = [1, 2, 3]
    nextPermutation(nums1)
    print(f"Input: [1,2,3]")
    print(f"Output: {nums1}")
    print(f"Expected: [1,3,2]")
    print()

    # Test case 2
    print("Test 2:")
    nums2 = [3, 2, 1]
    nextPermutation(nums2)
    print(f"Input: [3,2,1]")
    print(f"Output: {nums2}")
    print(f"Expected: [1,2,3]")
    print()

    # Test case 3
    print("Test 3:")
    nums3 = [1, 1, 5]
    nextPermutation(nums3)
    print(f"Input: [1,1,5]")
    print(f"Output: {nums3}")
    print(f"Expected: [1,5,1]")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)