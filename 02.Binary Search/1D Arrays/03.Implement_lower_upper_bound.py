# Test case 1
# TIME COMPLEXITY: O(NlogN)

def lowerbound(int arr[], int n, int x): low = 0, high = n-1 ans = -1 while(low<=high) mid = low+(high-low)/2 if(arr[mid]<=x) ans = mid low = mid+1 else high = mid-1 if(ans not =-1) ans = arr[ans] return ans def upperbound(int arr[], int n, int x): low = 0, high = n-1 ans = -1 while(low<=high) mid = low+(high-low)/2 if(arr[mid]>=x) ans = mid high = mid-1 else low = mid+1 if(ans not =-1) ans = arr[ans] return ans pair<int, int> getFloorAndCeil(int arr[], int n, int x) sort(arr,arr+n) Floor = lowerbound(arr,n,x) Ceil = upperbound(arr,n,x) return Floor,Ceil
# SPACE COMPLEXITY = O(1)
```
