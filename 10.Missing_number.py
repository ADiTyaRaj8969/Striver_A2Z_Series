# QUESTION:-
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1: Input: nums = [3,0,1], Output: 2
# Example 2: Input: nums = [0,1], Output: 2

# APPROACH:-
# Calculate the optimum sum (sum when all elements were present)
# Calculate the actual array's sum
# Return the optimum sum - actual sum

# CODE:-
def missingNumber(nums):
    """Find the missing number in range [0, n]"""
    n = len(nums)
    optimum_sum = (n * (n + 1)) // 2  # sum of 0 to n
    actual_sum = sum(nums)
    return optimum_sum - actual_sum


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    nums1 = [3, 0, 1]
    result1 = missingNumber(nums1)
    print(f"Output: {result1}")
    print("Expected: 2")
    print()
    
    # Test case 2
    print("Test 2:")
    nums2 = [0, 1]
    result2 = missingNumber(nums2)
    print(f"Output: {result2}")
    print("Expected: 2")

# TIME COMPLEXITY = O(N) 
