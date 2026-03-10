# Test case 1
# Test case 2
# TIME COMPLEXITY: O(log N), where N is the size of the array.

def countOccurrences(int arr[], int n, int x): first = lower_bound(arr, arr + n, x) - arr if (first == n or arr[first] not = x) return 0 last = upper_bound(arr, arr + n, x) - arr return last - first
# SPACE COMPLEXITY = O(1)
```
