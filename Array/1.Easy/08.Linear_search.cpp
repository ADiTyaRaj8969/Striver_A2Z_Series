/*
I don't think anyone needs it's solution. The idea is to traverse the array using loop and when the element
is equal to k return the same
*/

#include <bits/stdc++.h>
using namespace std;

// CODE:-
int linearSearch(int arr[], int n, int k)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == k)
            return i;
    }
    return -1;
}

int main()
{
    int arr[] = {5, 3, 7, 2, 8, 1, 9};
    int n = 7;
    int k = 8;
    
    cout << "Array: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    int index = linearSearch(arr, n, k);
    
    if (index != -1)
        cout << "Element " << k << " found at index: " << index << endl;
    else
        cout << "Element " << k << " not found" << endl;
    
    return 0;
}

// TIME COMPLEXITY = O(N)
