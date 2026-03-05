# QUESTION:-
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# APPROACH:-
# The idea is while traversing the array if we found any zero then we have to swap it with next non-zero

# CODE:-
def moveZeroes(nums):
    """Move all zeros to the end while maintaining relative order of non-zero elements"""
    # Find the position where we should place non-zero elements
    insert_pos = 0
    
    # Move all non-zero elements to the front
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    
    # Fill remaining positions with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print("Original array:", nums)
    moveZeroes(nums)
    print("After moving zeros to end:", nums)
    # Expected: [1, 3, 12, 0, 0]

# TIME COMPLEXITY = O(N) (as we moving through the array only once) 
