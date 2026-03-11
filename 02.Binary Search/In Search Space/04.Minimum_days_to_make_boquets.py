# we can only make one bouquet.
# we can only make two bouquets.
# we can make 3 bouquets. The answer is 3.
# if((long)mk > bloomDay.size())
# Test case 1
# Time Complexity: The binary search approach takes O(log n), where n is the number of elements in the `bloomDay` array.
# Space Complexity: The space complexity is O(1) since we are using a constant amount of extra space.

def isPossible(int mid, & bloomDay, int m, int k): bqts = 0, temp = 0 for(auto it:bloomDay) if(it<=mid) temp++ else temp = 0 if(temp==k) bqts++ temp = 0 if(bqts>=m) return true return false def minDays(& bloomDay, int m, int k): if((long)m*k > bloomDay).__len__()) return -1 ans = -1 low = INT_MAX, high = INT_MIN for(auto it:bloomDay) low = min(low,it) high = max(high,it) while(low<=high) mid = low+(high-low)/2 if(isPossible(mid,bloomDay,m,k)) ans = mid high = mid-1 else low = mid+1 return ans

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
```
