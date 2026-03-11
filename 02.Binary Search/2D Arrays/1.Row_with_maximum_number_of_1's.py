# {0, 1, 1, 1}
# {0,  0,  1,  1}
# out of matrix  {1,  1,  1,  1} ---> ans
# CODE:-
# Test case 1
# TIME COMPLEXITY = O(N+M)
# SPACE COMPLEXITY = O(1)

- def rowWithMax1s(> arr, int n, int m): j = m - 1 i = 0 ans = -1 while (j >= 0 and i < n) while (arr[i][j] == 1) ans = i j-- if (i < n) i++ return ans
```
