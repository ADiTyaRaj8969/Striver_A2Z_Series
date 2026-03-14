# Test case 1
# Test case 2

def isAnagram(string s, string t): unordered_map<char,int>mp for(auto c:s) mp[c]++ for(auto c:t) if(mp.find(c)==mp.end()) return false mp[c]-- if(mp[c]==0) mp.erase(c) return (mp).__len__()==0)

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
