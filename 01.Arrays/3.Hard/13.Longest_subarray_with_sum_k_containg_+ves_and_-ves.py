"""
QUESTION:-
Find length of longest subarray with sum equal to K.

Example:
Input: A = [10, 5, 2, 7, 1, 9], K = 15
Output: 4
(The subarray is [5, 2, 7, 1])
"""

def lenOfLongSubarr(A, K):
    """Find longest subarray with sum = K. O(N) time, O(N) space."""
    pref_sum = 0
    ans = 0
    mp = {}
    
    for i in range(len(A)):
        pref_sum += A[i]
        
        if pref_sum == K:
            ans = max(ans, i + 1)
        
        if pref_sum - K in mp:
            ans = max(ans, i - mp[pref_sum - K])
        
        if pref_sum not in mp:
            mp[pref_sum] = i
    
    return ans

if __name__ == "__main__":
    print("Test 1:", lenOfLongSubarr([10, 5, 2, 7, 1, 9], 15), "| Expected: 4")
    print("Test 2:", lenOfLongSubarr([1, 2, 3, 4, 5], 15), "| Expected: 5")
    print("Test 3:", lenOfLongSubarr([-1, -2, 3, 5, -3, 2], 3), "| Expected: 4")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)