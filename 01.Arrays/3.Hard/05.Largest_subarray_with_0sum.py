"""
QUESTION:-
Find length of longest subarray with sum = 0.

Example:
Input: A = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5 (subarray [-2, 2, -8, 1, 7])
"""

def maxLen(arr):
    """Find longest subarray with sum 0. O(N) time & space."""
    prefix_sum = 0
    sum_map = {0: -1}
    max_length = 0
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum in sum_map:
            max_length = max(max_length, i - sum_map[prefix_sum])
        else:
            sum_map[prefix_sum] = i
    
    return max_length

if __name__ == "__main__":
    print("Test 1:", maxLen([15, -2, 2, -8, 1, 7, 10, 23]), "| Expected: 5")
    print("Test 2:", maxLen([1, -1, 3, 3]), "| Expected: 2")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)