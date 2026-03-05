# QUESTION:-
# Given a sorted integer array nums, remove duplicates in-place such that each unique element appears only once.
# Return the number of unique elements k. Modify nums so first k elements are unique.
# Example 1: Input: nums = [1,1,2], Output: 2, nums = [1,2,_]
# Example 2: Input: nums = [0,0,1,1,1,2,2,3,3,4], Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# APPROACH:-
# Keep a pointer k which signifies array is unique up to index k
# Traverse array and if nums[k] != nums[j], increment k and swap nums[k] with nums[j]
# Return k+1 (due to 0-based indexing)

# CODE:-
def removeDuplicates(nums):
    """Remove duplicates from sorted array"""
    if len(nums) == 0:
        return 0
    
    k = 0  # up to k array contains unique elements
    for j in range(1, len(nums)):
        if nums[k] != nums[j]:
            k += 1
            nums[k], nums[j] = nums[j], nums[k]  # swap
    return k + 1


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [1, 1, 2]
    result1 = removeDuplicates(nums1)
    print(f"Output: {result1}, nums = {nums1}")
    print(f"Expected: 2, nums = [1, 2, ...]")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result2 = removeDuplicates(nums2)
    print(f"Output: {result2}, nums = {nums2[:result2]}")
    print(f"Expected: 5")

# TIME COMPLEXITY = O(N) 
