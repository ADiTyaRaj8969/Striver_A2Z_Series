# Test case 1

def reverseWords(string s): ans = "" start = -1, end = -1 for(int i=0 i<s).__len__() i++) while(s[i]==' ') i++ start = i while(i<s).__len__() and s[i] not =' ') i++ end = i temp = s.substr(start,end-start) reverse(temp.begin(),temp.end()) ans = ans+" "+temp reverse(ans.begin(),ans.end()) i = 0, j=ans).__len__()-1 while(ans[i]==' ') i++ while(ans[j]==' ') j-- ans = ans.substr(i,j-i+1) return ans

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
```
