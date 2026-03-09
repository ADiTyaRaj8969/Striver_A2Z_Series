# Test case 1
# Test case 2
# TIME COMPLEXITY: O(log N)

def findFloor( v, long long n, long long x): long low = 0, high = n - 1 ans = -1 while (low <= high) long mid = low + (high - low) / 2 if (v[mid] <= x) ans = mid low = mid + 1 else high = mid - 1 return ans
# SPACE COMPLEXITY = O(1)
```
