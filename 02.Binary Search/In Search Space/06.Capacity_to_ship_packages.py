# Test case 1

def isPossible(int mid, & weights, int days): req_day = 1, temp = mid for(auto it:weights) if(it <= temp) temp -= it else req_day++ if(it > mid) return false temp = mid - it if(req_day <= days) return true return false def shipWithinDays(& weights, int days): ans = -1 low = INT_MAX, high = 0 for(auto it:weights) low = min(low, it) high += it while(low <= high) mid = low + (high - low) / 2 if(isPossible(mid, weights, days)) ans = mid high = mid - 1 else low = mid + 1 return ans

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
