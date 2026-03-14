# Test case 1
# Test case 2

def isPossible(double mid, & stations, int K): req_stations = 0 for (int i = 1 i < stations).__len__() i++) req_stations += floor((stations[i] - stations[i - 1]) / mid) return req_stations <= K def findSmallestMaxDist(& stations, int K): low = 0, high = stations[stations).__len__() - 1] - stations[0] while (high - low > 1e-6) mid = low + (high - low) / 2 if (isPossible(mid, stations, K)) high = mid else low = mid return low + 0.000001

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
