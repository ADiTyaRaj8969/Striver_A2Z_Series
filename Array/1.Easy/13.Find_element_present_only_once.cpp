/*
QUESTION:-
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
*/


#include <bits/stdc++.h>
using namespace std;
/*
APPROACH:-
-> We can use XOR operation as we know xor cancles out the same elements
-> Intial xr=0 then traverse the entire array and xor each element with xr
-> Since only one element is present once and all other are present twice so the remaining element would be the
    one which is present only once cause all other gets cancels out
*/

// CODE:-
int singleNumber(vector<int> &nums)
{
    int xr = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        xr = nums[i] ^ xr;
    }
    return xr;
}


int main() {
    // Test case 1
    cout << "Test 1:" << endl;
    vector<int> nums1 = {2,2,1};
    int result1 = singleNumber(nums1);
    cout << "Output: " << result1 << endl;
    cout << "Expected: 1" << endl;
    cout << endl;

    // Test case 2
    cout << "Test 2:" << endl;
    vector<int> nums2 = {4,1,2,1,2};
    int result2 = singleNumber(nums2);
    cout << "Output: " << result2 << endl;
    cout << "Expected: 4" << endl;
    cout << endl;

    return 0;
}

// TIME COMPLEXITY = O(N)
