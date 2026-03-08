"""
QUESTION:-
Find all elements appearing more than ⌊n/3⌋ times.

Example:
Input: nums = [3,2,3]
Output: [3]
"""

def majorityElement(nums):
    """Find all elements appearing more than n/3 times. O(N) time, O(1) space."""
    n = len(nums)
    c1, c2 = None, None
    vote1, vote2 = 0, 0
    
    # Find potential candidates using Boyer-Moore voting
    for num in nums:
        if c1 == num:
            vote1 += 1
        elif c2 == num:
            vote2 += 1
        elif vote1 == 0:
            c1, vote1 = num, 1
        elif vote2 == 0:
            c2, vote2 = num, 1
        else:
            vote1 -= 1
            vote2 -= 1
    
    # Count and verify candidates
    cnt1 = cnt2 = 0
    for num in nums:
        if num == c1:
            cnt1 += 1
        elif num == c2:
            cnt2 += 1
    
    ans = []
    if cnt1 > n // 3:
        ans.append(c1)
    if cnt2 > n // 3 and c2 != c1:
        ans.append(c2)
    return ans

if __name__ == "__main__":
    print("Test 1:", majorityElement([3,2,3]), "| Expected: [3]")
    print("Test 2:", majorityElement([1]), "| Expected: [1]")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)