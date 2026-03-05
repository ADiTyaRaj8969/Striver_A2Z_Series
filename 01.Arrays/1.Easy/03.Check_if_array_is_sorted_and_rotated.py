# QUESTION:-
# Given an array nums, return true if the array was originally sorted in non-decreasing order,
# then rotated some number of positions (including zero). Otherwise, return false.
# Example 1: Input: nums = [3,4,5,1,2], Output: true
# Explanation: [1,2,3,4,5] is the original sorted array, rotated by 3 positions

# APPROACH:-
# Compare all neighbor elements (a,b) in array
# The case of a > b can happen at most once
# If all a <= b, array is already sorted, return true
# If only one a > b and first element >= last element, array is sorted and rotated

# CODE:-
def check(nums):
    """Check if array is sorted and rotated"""
    cnt = 0
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            cnt += 1
    
    if cnt == 0:
        return True
    elif cnt == 1 and nums[0] >= nums[n - 1]:
        return True
    return False


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [3, 4, 5, 1, 2]
    result1 = check(nums1)
    print(f"Output: {result1}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [2, 1, 3, 4]
    result2 = check(nums2)
    print(f"Output: {result2}")
    print(f"Expected: False")

# TIME COMPLEXITY = O(N) 
