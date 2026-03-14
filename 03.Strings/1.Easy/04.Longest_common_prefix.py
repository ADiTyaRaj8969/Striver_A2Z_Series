# Time Complexity: O(NMlog(N)), where N is the number of strings and M is the maximum length of the strings.
# - Sorting the array of strings takes O(Nlog(N)) time.
# TODO: Extract test cases from the examples above
# Call your function: longestCommonPrefix()
# Print string result:
# cout << "Result: " << result << endl;

def longestCommonPrefix(& strs): if (strs.empty()) return "" sort(strs.begin(), strs.end()) first = 0, last = strs).__len__() - 1 i = 0, j = 0 len = 0 while (i < strs[first]).__len__() and j < strs[last]).__len__() and strs[first][len] == strs[last][len]) i++ j++ len++ return strs[first].substr(0, len)

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)
```
