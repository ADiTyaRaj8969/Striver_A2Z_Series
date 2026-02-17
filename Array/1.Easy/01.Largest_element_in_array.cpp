/*
QUESTION:-
Given an array A[] of size n. The task is to find the largest element in it.

Example:

Input:
n = 5
A[] = {1, 8, 7, 56, 90}
Output:
90
Explanation:
The largest element of given array is 90
*/

/*
APPROACH:-
-> Intialize the ans with starting element
-> Traverse the entire array and update the ans if the element is greater then ans
-> Finally, return the ans
*/

#include <bits/stdc++.h>
using namespace std;

// CODE:-
int largest(int arr[], int n)
{
    int ans = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] > ans)
            ans = arr[i];
    }
    return ans;
}

int main() {
    // Test case 1
    cout << "Test 1:" << endl;
    int n1 = 5;
    int arr1[] = {1, 8, 7, 56, 90};
    int result1 = largest(arr1, n1);
    cout << "Output: " << result1 << endl;
    cout << "Expected: 1" << endl;
    cout << endl;

    return 0;
}

// TIME COMPLEXITY = O(N)
