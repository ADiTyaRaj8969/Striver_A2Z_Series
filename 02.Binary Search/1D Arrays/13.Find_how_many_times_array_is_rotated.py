# Test case 1
# TIME COMPLEXITY: O(log n)

def findKRotation(int arr[], int n): low = 0, high = n - 1 while (low < high) mid = low + (high - low) / 2 if (arr[mid] > arr[n - 1]) low = mid + 1 else high = mid return low
# SPACE COMPLEXITY = O(1)
```
