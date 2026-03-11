# Test case 1
# Test case 2

def max_finder(& row): maxi = INT_MIN ans = -1 for (int i = 0 i < row).__len__() i++) if (row[i] > maxi) maxi = row[i] ans = i return ans def findPeakGrid(>& mat): n = mat).__len__() low = 0, high = n - 1 while (low <= high) mid = low + (high - low) / 2 col = max_finder(mat[mid]) if ((mid == 0 or mat[mid][col] > mat[mid - 1][col]) and (mid == n - 1 or mat[mid][col] > mat[mid + 1][col])) return mid, col else if (mid not = 0 and mat[mid][col] < mat[mid - 1][col]) high = mid - 1 else low = mid + 1 return -1, -1

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(N)
```
