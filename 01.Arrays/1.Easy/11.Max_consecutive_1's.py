# QUESTION:-
# Find the maximum count of consecutive 1's in a given integer array nums containing only 0's and 1's.
# Example 1: Input: [1,1,0,1,1,1], Output: 3
# Example 2: Input: [1,0,1,1,0,1], Output: 2

# APPROACH:-
# Traverse the entire array
# Within it run a loop while elements are equal to 1 and store the count
# Update the ans as max(ans, cnt)

# CODE:-
def findMaxConsecutiveOnes(nums):
    """Find the maximum count of consecutive 1's"""
    ans = 0
    i = 0
    while i < len(nums):
        cnt = 0  # to store the count of consecutive 1's
        while i < len(nums) and nums[i] == 1:
            cnt += 1
            i += 1
        ans = max(ans, cnt)
        if i < len(nums):
            i += 1  # move past the 0
    return ans


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [1, 1, 0, 1, 1, 1]
    result1 = findMaxConsecutiveOnes(nums1)
    print(f"Output: {result1}")
    print("Expected: 3")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [1, 0, 1, 1, 0, 1]
    result2 = findMaxConsecutiveOnes(nums2)
    print(f"Output: {result2}")
    print("Expected: 2")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
