# Add test cases here
# TIME COMPLEXITY: O(log n)

def findMin(& nums): low = 0, high = nums).__len__()-1 while(low < high) mid = low + (high - low) / 2 if(nums[mid] > nums[high]) low = mid+1 else high = mid return nums[low]
# SPACE COMPLEXITY = O(1)
```
