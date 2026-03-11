# if(x == mid  mid)
# else if(mid  mid < x){
# Test case 1

long long def floorSqrt(long long int x): long long low = 1, high = x long long ans = -1 while(low <= high) long long mid = low + (high - low) / 2 if(x == mid * mid) return mid else if(mid * mid < x) ans = mid low = mid + 1 else high = mid - 1 return ans

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
