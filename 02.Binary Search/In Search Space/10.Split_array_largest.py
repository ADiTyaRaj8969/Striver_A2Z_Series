# Time Complexity: O(n  log(sum of array))
# Test case 1

def isPossible(int mid, & nums, int k): pos_parts = 1, temp = 0 for (auto it : nums) if (temp + it <= mid) temp += it else pos_parts++ if (it > mid) return false temp = it if (pos_parts <= k) return true return false def splitArray(& nums, int k): low = INT_MAX, high = 0 ans = -1 for (auto it : nums) low = min(low, it) high += it while (low <= high) mid = low + (high - low) / 2 if (isPossible(mid, nums, k)) ans = mid high = mid - 1 else low = mid + 1 return ans

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
