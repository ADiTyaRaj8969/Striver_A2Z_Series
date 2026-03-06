# QUESTION:-
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than floor(n/2) times.
# Example 1: Input: nums = [3,2,3], Output: 3
# Example 2: Input: nums = [2,2,1,1,1,2,2], Output: 2

# APPROACH:-
# Use Boyer-Moore Voting Algorithm
# Initialize candidate = first element, vote = 1
# For each element:
#   If vote == 0, update candidate to current element
#   If element == candidate, vote++, else vote--
# Return candidate

# CODE:-
def majorityElement(nums):
    """Find the majority element using Boyer-Moore Voting Algorithm"""
    candidate = nums[0]
    vote = 1
    
    for i in range(1, len(nums)):
        if vote == 0:
            candidate = nums[i]
            vote = 1
        elif nums[i] == candidate:
            vote += 1
        else:
            vote -= 1
    
    return candidate


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [3, 2, 3]
    result1 = majorityElement(nums1)
    print(f"Output: {result1}")
    print("Expected: 3")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = majorityElement(nums2)
    print(f"Output: {result2}")
    print("Expected: 2")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
