"""
QUESTION:-
Count subarrays with XOR equal to k.

Example:
Input: A = [1, 2, 3, 2], k = 2
Output: 3
"""

def subarraysWithSumK(nums, k):
    """Count subarrays with XOR = k. O(N) time & space."""
    prefix_xor = 0
    count = 0
    xor_map = {0: 1}
    
    for num in nums:
        prefix_xor ^= num
        if prefix_xor ^ k in xor_map:
            count += xor_map[prefix_xor ^ k]
        xor_map[prefix_xor] = xor_map.get(prefix_xor, 0) + 1
    
    return count

if __name__ == "__main__":
    print("Test 1:", subarraysWithSumK([1, 2, 3, 2], 2), "| Expected: 3")
    print("Test 2:", subarraysWithSumK([5, 2, 3, 3], 4), "| Expected: 2")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)