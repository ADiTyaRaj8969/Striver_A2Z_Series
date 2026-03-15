# Question:
# 2 loops to generate all substrings
# Test case 1

def get_maxmin(& freq): maxi = INT_MIN, mini = INT_MAX for(auto it:freq) maxi = max(maxi,it) if(it not =0) mini = min(mini,it) return (mini==INT_MAX)?0:maxi-mini def beautySum(string s): ans = 0 

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
