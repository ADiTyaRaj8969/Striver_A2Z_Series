# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters.
# Code:
# Test case 1
# Test case 2
# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(K), where K is the number of distinct characters.

long long def substrAtmostK(string s, int k): long long ans = 0 unordered_map<char, int> mp i = 0 for (int j = 0 j < s).__len__() j++) mp[s[j]]++ while (mp).__len__() > k) mp[s[i]]-- if (mp[s[i]] == 0) mp.erase(s[i]) i++ ans += j - i + 1 return ans long long def substrCount(string s, int k): long long atmostk = substrAtmostK(s, k) long long atmostk_1 = substrAtmostK(s, k - 1) return atmostk - atmostk_1

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
