# QUESTION:
# Given a row-wise sorted matrix of size RC where R and C are always odd, find the median of the matrix.
# CODE:
# int opt_cnt = (R  C + 1) / 2;
# Test case 1
# TIME COMPLEXITY: O(R  log(C)  log(range)), where R is the number of rows, C is the number of columns, and range is the difference between the minimum and maximum elements in the matrix.

def median(>& matrix, int R, int C): low = INT_MAX high = INT_MIN opt_cnt = (R * C + 1) / 2 ans = -1 for i in range(0, R) low = min(low, matrix[i][0]) high = max(high, matrix[i][C - 1]) while (low <= high) mid = low + (high - low) / 2 cnt = 0 for i in range(0, R) cnt += upper_bound(matrix[i].begin(), matrix[i].end(), mid) - matrix[i].begin() if (cnt < opt_cnt) low = mid + 1 else ans = mid high = mid - 1 return ans
# SPACE COMPLEXITY = O(1)
```
