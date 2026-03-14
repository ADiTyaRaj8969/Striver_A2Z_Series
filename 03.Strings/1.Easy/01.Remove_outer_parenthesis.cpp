/*
Question:
Given a valid parentheses string `s`, remove the outermost parentheses of every primitive string in the primitive decomposition of `s`.

Approach:
- We can iterate through the characters of the string and keep track of the number of open parentheses encountered.
- Whenever we encounter an opening parenthesis, if the count of open parentheses is greater than 0, we append it to the result string.
- When we encounter a closing parenthesis, we decrement the count of open parentheses and append it to the result string only if the count is greater than 1.

Code:
*/

#include <bits/stdc++.h>
using namespace std;
string removeOuterParentheses(string s) {
    string res;
    int opened = 0;

    for (auto c : s) {
        if (c == '(') {
            if (opened > 0)
                res += c;
            opened++;
        } else {
            if (opened > 1)
                res += c;
            opened--;
        }
    }

    return res;
}

int main() {
    // Test case 1
    string s1 = "(()())(())";
    string result1 = removeOuterParentheses(s1);
    cout << "Input: s = \"" << s1 << "\"" << endl;
    cout << "Output: \"" << result1 << "\"" << endl;
    
    // Test case 2
    string s2 = "(()())(())(()(()))";
    string result2 = removeOuterParentheses(s2);
    cout << "
Input: s = \"" << s2 << "\"" << endl;
    cout << "Output: \"" << result2 << "\"" << endl;
    
    return 0;
}

/*
Time Complexity: O(N), where N is the length of the input string `s`.
Space Complexity: O(N), where N is the length of the input string `s`.
*/