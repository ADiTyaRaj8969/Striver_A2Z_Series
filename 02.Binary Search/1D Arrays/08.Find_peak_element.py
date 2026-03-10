# Test case 1
# Test case 2
# TIME COMPLEXITY: O(log n)

def findPeakElement(& nums): low = 0, high = nums).__len__()-1 while(low < high) mid = low + (high - low) / 2 if(nums[mid] < nums[mid+1]) low = mid+1 else high = mid return low
# SPACE COMPLEXITY = O(1)
```
