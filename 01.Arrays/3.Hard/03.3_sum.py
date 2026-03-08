"""
QUESTION:-
Return all triplets [i, j, k] that sum to 0.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""

def threeSum(nums):
    """Find all unique triplets summing to zero. O(N^2) time."""
    nums.sort()
    ans = []
    n = len(nums)
    
    for k in range(n):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        
        target = -nums[k]
        i, j = k + 1, n - 1
        
        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == target:
                ans.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        
        while k + 1 < n and nums[k + 1] == nums[k]:
            k += 1
    
    return ans

if __name__ == "__main__":
    print("Test 1:", threeSum([-1, 0, 1, 2, -1, -4]))
    print("Expected: [[-1, -1, 2], [-1, 0, 1]]")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)