"""
QUESTION:-
Return all unique quadruplets [a, b, c, d] that sum to target.

Example:
Input: nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""

def fourSum(nums, target):
    """Find all unique quadruplets summing to target. O(N^3) time."""
    nums.sort()
    ans = []
    n = len(nums)
    
    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
            break
        
        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
            if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target:
                break
            
            c, d = b + 1, n - 1
            remaining = target - nums[a] - nums[b]
            
            while c < d:
                current_sum = nums[c] + nums[d]
                if current_sum == remaining:
                    ans.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
                    d -= 1
                    while c < d and nums[c] == nums[c - 1]:
                        c += 1
                    while c < d and nums[d] == nums[d + 1]:
                        d -= 1
                elif current_sum < remaining:
                    c += 1
                else:
                    d -= 1
        
        while a + 1 < n and nums[a + 1] == nums[a]:
            a += 1
    
    return ans

if __name__ == "__main__":
    print("Test 1:", fourSum([1, 0, -1, 0, -2, 2], 0))

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)