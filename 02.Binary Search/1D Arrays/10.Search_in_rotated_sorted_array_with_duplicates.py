# Test case 1
# Test case 2
# TIME COMPLEXITY: O(log n)

def search(& nums, int target): low = 0, high = nums).__len__() - 1 while (low <= high) mid = low + (high - low) / 2 if (nums[mid] == target) return true if (nums[mid] == nums[low] and nums[mid] == nums[high]) low++ high-- continue if (nums[low] <= nums[mid]) if (nums[low] <= target and target <= nums[mid]) high = mid - 1 else low = mid + 1 else if (nums[mid] <= target and target <= nums[high]) low = mid + 1 else high = mid - 1 return false
# SPACE COMPLEXITY = O(1)
```
