# Add test cases here
# TIME COMPLEXITY: O(log n)

def singleNonDuplicate(& nums): low = 0, high = nums).__len__() - 1 while (low < high) mid = low + (high - low) / 2 if (mid % 2 == 0) if (nums[mid] == nums[mid + 1]) low = mid + 1 else high = mid else if (nums[mid] not = nums[mid + 1]) low = mid + 1 else high = mid return nums[low]
# SPACE COMPLEXITY = O(1)
```
