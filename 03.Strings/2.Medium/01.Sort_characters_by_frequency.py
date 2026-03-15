# TODO: Extract test cases from the examples above
# Call your function: frequencySort()
# Print string result:
# cout << "Result: " << result << endl;

def frequencySort(string s): unordered_map<char, int> mp for (auto c : s) mp[c]++ priority_queue<pair<int, char>> pq for (auto it : mp) pq.push( it.second, it.first ) ans = "" while ( not pq.empty()) auto curr = pq.top() pq.pop() ans.append(curr.first, curr.second) return ans

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)
```
