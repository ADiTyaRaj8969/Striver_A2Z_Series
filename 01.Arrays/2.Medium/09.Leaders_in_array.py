"""
QUESTION:-
Given an array A of positive integers. Your task is to find the leaders in the array.
An element of the array is a leader if it is greater than or equal to all the elements to its right side.
The rightmost element is always a leader.

Example 1:
Input: A = [16,17,4,3,5,2]
Output: [17, 5, 2]
Explanation: 17 is greater than all elements to its right.
5 is greater than 2. 2 is the rightmost element.
"""

# APPROACH:-
# Traverse the array from right to left.
# Keep track of the maximum element seen so far.
# If current element is >= maximum, it's a leader.

# CODE:-

def leaders(arr):
    """
    Find all leaders in the array (elements >= all elements to their right).
    
    Time Complexity: O(N)
    Space Complexity: O(K) where K is number of leaders
    """
    if not arr:
        return []
    
    ans = []
    n = len(arr)
    
    # Start with rightmost element (always a leader)
    max_from_right = arr[n - 1]
    ans.append(max_from_right)
    
    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            ans.append(arr[i])
            max_from_right = arr[i]
    
    # Reverse to get the answer in original order
    ans.reverse()
    return ans


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    arr1 = [16, 17, 4, 3, 5, 2]
    result1 = leaders(arr1)
    print(f"Input: {arr1}")
    print(f"Output: {result1}")
    print(f"Expected: [17, 5, 2]")
    print()

    # Test case 2
    print("Test 2:")
    arr2 = [1, 2, 3, 4, 5]
    result2 = leaders(arr2)
    print(f"Input: {arr2}")
    print(f"Output: {result2}")
    print(f"Expected: [5]")
    print()

    # Test case 3
    print("Test 3:")
    arr3 = [5, 4, 3, 2, 1]
    result3 = leaders(arr3)
    print(f"Input: {arr3}")
    print(f"Output: {result3}")
    print(f"Expected: [5, 4, 3, 2, 1]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)