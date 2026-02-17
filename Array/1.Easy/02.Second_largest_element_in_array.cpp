/*
QUESTION:-
Given an array Arr of size N, print second largest distinct element from an array.

Example:

Input:
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the
array is 35 and the second largest element
is 34.
*/

/*
APPROACH
-> If the current element is larger than 'large' then update second_large and large variables
-> Else if the current element is larger than 'second_large' then we update the variable second_large.
-> Once we traverse the entire array, we would find the second largest element in the variable second_large.
*/

#include <bits/stdc++.h>
using namespace std;

// CODE:-
int print2largest(int arr[], int n)
{
    int prev = -1, curr = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] > curr)
        {
            prev = curr;
            curr = arr[i];
        }
        else if (arr[i] > prev && arr[i] != curr)
            prev = arr[i];
    }
    return prev;
}

int main() {
    // Test case 1
    cout << "Test 1:" << endl;
    int N1 = 6;
    int arr1[] = {12, 35, 1, 10, 34, 1};
    int result1 = print2largest(arr1, N1);
    cout << "Output: " << result1 << endl;
    cout << "Expected: 34" << endl;
    cout << endl;

    return 0;
}

// TIME COMPLEXITY = O(N)
