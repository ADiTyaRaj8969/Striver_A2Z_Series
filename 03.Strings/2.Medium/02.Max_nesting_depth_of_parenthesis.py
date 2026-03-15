# TODO: Extract test cases from the examples above
# Call your function: maxDepth()
# Print result:
# cout << "Result: " << result << endl;

def maxDepth(string s): opened = 0, ans = 0 for (auto c : s) if (c == '(') opened++ ans = max(ans, opened) else if (c == ')') opened-- return ans

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
