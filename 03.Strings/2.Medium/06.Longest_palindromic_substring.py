# Code:
# For odd length palindromes
# For even length palindromes
# Test case 1
# Test case 2

def expandFromCenter(string s, int start, int end, ans_start, ans_end, maxLen): while (start >= 0 and end < s).__len__() and s[start] == s[end]) if (end - start + 1 > maxLen) ans_start = start ans_end = end maxLen = end - start + 1 start-- end++ def longestPalindrome(string s): ans = "" maxLen = 0, ans_start = -1, ans_end = -1 for (int i = 0 i < s).__len__() i++) 

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
