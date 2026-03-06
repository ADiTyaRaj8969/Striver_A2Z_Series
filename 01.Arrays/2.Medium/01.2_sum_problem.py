# QUESTION:-
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example 1: Input: nums = [2,7,11,15], target = 9, Output: [0,1]
# Example 2: Input: nums = [3,2,4], target = 6, Output: [1,2]

# APPROACH:-
# Create a dictionary to store elements and their indices
# For each element, calculate complement = target - element
# If complement exists in dict, return indices
# Otherwise, add current element and index to dict

# CODE:-
def twoSum(nums, target):
    """Find two numbers that add up to target"""
    mp = {}  # dictionary to store element -> index
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in mp:
            return [i, mp[remain]]
        mp[nums[i]] = i
    return [-1, -1]  # No solution found


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    print(f"Output: {result1}")
    print("Expected: [0, 1]")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = twoSum(nums2, target2)
    print(f"Output: {result2}")
    print("Expected: [1, 2]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N) (for the hashmap)
