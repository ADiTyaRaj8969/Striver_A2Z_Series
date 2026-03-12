# Test case 1

def isPossible(int mid, int A[], int N, int M): pos_m = 1 temp = 0 for i in range(0, N) if (temp + A[i] <= mid) temp += A[i] else pos_m++ if (A[i] > mid) return false temp = A[i] if (pos_m <= M) return true return false def findPages(int A[], int N, int M): if (M > N) return -1 low = INT_MAX, high = 0 ans = -1 for i in range(0, N) low = min(low, A[i]) high += A[i] while (low <= high) mid = low + (high - low) / 2 if (isPossible(mid, A, N, M)) ans = mid high = mid - 1 else low = mid + 1 return ans

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(N)
```
