/*
QUESTION:-
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
*/


#include <bits/stdc++.h>
using namespace std;
/*
APPROACH:
To determine if a linked list is a palindrome, we can follow these steps:
1. Find the middle node of the linked list using the slow and fast pointer technique.
2. Reverse the second half of the linked list.
3. Compare the first half of the original linked list with the reversed second half.
4. If all nodes match, the linked list is a palindrome.
5. If any node does not match, the linked list is not a palindrome.
*/

ListNode* reverseLL(ListNode* start) {
    ListNode* prev = NULL;
    ListNode* curr = start;
    while (curr) {
        ListNode* frwd = curr->next;
        curr->next = prev;
        prev = curr;
        curr = frwd;
    }
    return prev;
}

bool isPalindrome(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    
    // Find the middle node using the slow and fast pointer technique
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Reverse the second half of the linked list
    ListNode* reversedHalf = reverseLL(slow);
    
    // Compare the first half with the reversed second half
    while (reversedHalf) {
        if (head->val != reversedHalf->val)
            return false;
        head = head->next;
        reversedHalf = reversedHalf->next;
    }
    
    return true;
}


int main() {
    // Test case 1
    cout << "Test 1:" << endl;
    vector<int> head1 = {1,2,2,1};
    bool result1 = isPalindrome(head1);
    cout << "Output: " << result1 << endl;
    cout << "Expected: true" << endl;
    cout << endl;

    // Test case 2
    cout << "Test 2:" << endl;
    vector<int> head2 = {1,2};
    bool result2 = isPalindrome(head2);
    cout << "Output: " << result2 << endl;
    cout << "Expected: false" << endl;
    cout << endl;

    return 0;
}

// TIME COMPLEXITY: O(N)


