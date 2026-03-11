# Test case 1

def NthRoot(int n, int m): low = 1, high = m while (low <= high) long mid = low + (high - low) / 2 if (pow(mid, n) == m) return mid else if (pow(mid, n) < m) low = mid + 1 else high = mid - 1 return -1

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
