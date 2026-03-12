# Test case 1

def isPossible(int mid, & position, int m): placeM = 1 start = 0 for(int i=1 i<position).__len__() i++) if(position[i]-position[start]>=mid) placeM++ start = i if(placeM>=m) return true return false def maxDistance(& position, int m): sort(position.begin(),position.end()) low = 1, high = position[position).__len__()-1]-position[0] ans = -1 while(low<=high) mid = low+(high-low)/2 if(isPossible(mid,position,m)) ans = mid low = mid+1 else high = mid-1 return ans

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)
```
