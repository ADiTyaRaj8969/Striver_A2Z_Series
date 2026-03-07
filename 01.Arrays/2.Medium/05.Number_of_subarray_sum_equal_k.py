"""
QUESTION:-
Given an array of integers nums and an integer k, return the total number of 
subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [-1,-1,1,1,1,1,0,-1,-1,-1,-1,-1,1,1,1,1,0], k = 0
Output: 9
"""

# APPROACH:-
# Use prefix sum with a hashmap to track occurrences of each prefix sum.
# For each element, check if (prefix_sum - k) exists in the map.
# This tells us how many subarrays ending at current index have sum = k.

# CODE:-

def subarraySum(nums, k):
    """
    Find the number of subarrays with sum equal to k.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    prefix_sum = 0
    count_map = {0: 1}  # Initialize with 0 having count 1
    ans = 0
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists in map
        if prefix_sum - k in count_map:
            ans += count_map[prefix_sum - k]
        
        # Add current prefix_sum to map
        count_map[prefix_sum] = count_map.get(prefix_sum, 0) + 1
    
    return ans


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = subarraySum(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print()

    # Test case 2
    print("Test 2:")
    nums2 = [-1, -1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, 1, 1, 1, 1, 0]
    k2 = 0
    result2 = subarraySum(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: 9")
    print()

    # Test case 3
    print("Test 3:")
    nums3 = [1]
    k3 = 1
    result3 = subarraySum(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: 1")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)