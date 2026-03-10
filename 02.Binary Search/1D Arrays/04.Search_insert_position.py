# Test case 1
# Test case 2
# TIME COMPLEXITY: O(log n) due to the use of lower_bound function

def searchInsert(& nums, int target): auto ans = lower_bound(nums.begin(), nums.end(), target) - nums.begin() return ans
# SPACE COMPLEXITY = O(1)
```
