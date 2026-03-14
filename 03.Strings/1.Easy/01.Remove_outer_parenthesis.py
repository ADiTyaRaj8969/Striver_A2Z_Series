# Test case 1
# Test case 2

def removeOuterParentheses(string s): string res opened = 0 for (auto c : s) if (c == '(') if (opened > 0) res += c opened++ else if (opened > 1) res += c opened-- return res

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
