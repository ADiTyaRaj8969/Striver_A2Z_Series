# Test case 1

def findKthPositive(& arr, int k): low = 0, high = arr).__len__() - 1 pos = -1 while (low <= high) mid = low + (high - low) / 2 if ((arr[mid] - (mid + 1)) < k) low = mid + 1 else pos = mid high = mid - 1 if (pos == -1) return arr).__len__() + k return pos + k

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
