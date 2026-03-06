# QUESTION:-
# Given an array nums with objects colored red (0), white (1), or blue (2), sort them in-place.
# Example 1: Input: nums = [2,0,2,1,1,0], Output: [0,0,1,1,2,2]
# Example 2: Input: nums = [2,0,1], Output: [0,1,2]

# APPROACH:-
# Use three pointers: low (left), mid (middle), high (right)
# If nums[mid] == 0: swap with low, increment both low and mid
# If nums[mid] == 1: just increment mid
# If nums[mid] == 2: swap with high, decrement high

# CODE:-
def sortColors(nums):
    """Sort array containing only 0s, 1s, and 2s (Dutch National Flag problem)"""
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [2, 0, 2, 1, 1, 0]
    sortColors(nums1)
    print(f"Output: {nums1}")
    print("Expected: [0, 0, 1, 1, 2, 2]")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [2, 0, 1]
    sortColors(nums2)
    print(f"Output: {nums2}")
    print("Expected: [0, 1, 2]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)

 
