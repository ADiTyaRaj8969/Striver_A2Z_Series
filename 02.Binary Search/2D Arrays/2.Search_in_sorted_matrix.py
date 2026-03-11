# You must write a solution in O(log(m  n)) time complexity.
# -> Since the array is sorted we can use binary search low = 0 and high = nm-1 i.e. total number of elements
# CODE:-
# int high = n  m - 1;
# Test case 1
# TIME COMPLEXITY = O(log(M * N))
# SPACE COMPLEXITY = O(1)

- def searchMatrix(> &matrix, int target): n = matrix).__len__() m = matrix[0]).__len__() low = 0 high = n * m - 1 while (low <= high) mid = low + (high - low) / 2 val = matrix[mid / m][mid % m] if (val == target) return true else if (val > target) high = mid - 1 else low = mid + 1 return false
```
