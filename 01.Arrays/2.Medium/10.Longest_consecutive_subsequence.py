"""
QUESTION:-
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

# APPROACH:-
# 1. Create a set of all numbers for O(1) lookup
# 2. For each number, check if it's the start of a sequence (num-1 not in set)
# 3. If it's a start, count consecutive elements from that number
# 4. Keep track of maximum length

# CODE:-

def longestConsecutive(nums):
    """
    Find the length of the longest consecutive elements sequence.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not nums:
        return 0
    
    # Create a set for O(1) lookup
    num_set = set(nums)
    max_length = 0
    
    for num in nums:
        # Check if this number can be the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive elements
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = longestConsecutive(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 4")
    print()

    # Test case 2
    print("Test 2:")
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = longestConsecutive(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 9")
    print()

    # Test case 3
    print("Test 3:")
    nums3 = [9, 1,4, 7, 3,2,8,5,6]
    result3 = longestConsecutive(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 9")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)