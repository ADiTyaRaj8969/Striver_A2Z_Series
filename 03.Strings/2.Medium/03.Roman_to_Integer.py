# result -= 2  symbolValues[s[i - 1]];
# Test case 1
# Test case 2

def romanToInt(string s): unordered_map<char, int> symbolValues = 'I', 1, 'V', 5, 'X', 10, 'L', 50, 'C', 100, 'D', 500, 'M', 1000 result = symbolValues[s[0]] for (int i = 1 i < s).__len__() i++) if (symbolValues[s[i]] > symbolValues[s[i - 1]]) result -= 2 * symbolValues[s[i - 1]] result += symbolValues[s[i]] else result += symbolValues[s[i]] return result

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
