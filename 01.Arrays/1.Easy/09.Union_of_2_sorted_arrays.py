# QUESTION:-
# Union of two arrays can be defined as the common and distinct elements in the two arrays.
# Given two sorted arrays of size n and m respectively, find their union.
# Example 1:
# Input: n = 5, arr1[] = {1, 2, 3, 4, 5}, m = 3, arr2 [] = {1, 2, 3}
# Output: 1 2 3 4 5

# APPROACH:-
# Take two pointer i and j where i is for arr1 and j is for arr2 and traverse
# While traversing 3 cases arise: arr1[i] < arr2[j], arr1[i] > arr2[j], arr1[i] == arr2[j]

# CODE:-
def findUnion(arr1, arr2, n, m):
    """Find union of two sorted arrays"""
    i = 0  # pointer for arr1
    j = 0  # pointer for arr2
    ans = []
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
            # Skip duplicates in arr1
            while i < n and arr1[i] == arr1[i - 1]:
                i += 1
        elif arr2[j] < arr1[i]:
            ans.append(arr2[j])
            j += 1
            # Skip duplicates in arr2
            while j < m and arr2[j] == arr2[j - 1]:
                j += 1
        else:  # arr1[i] == arr2[j]
            ans.append(arr1[i])
            i += 1
            j += 1
            # Skip duplicates in arr1
            while i < n and arr1[i] == arr1[i - 1]:
                i += 1
            # Skip duplicates in arr2
            while j < m and arr2[j] == arr2[j - 1]:
                j += 1
    
    # Add remaining elements from arr1
    while i < n:
        ans.append(arr1[i])
        i += 1
        while i < n and arr1[i] == arr1[i - 1]:
            i += 1
    
    # Add remaining elements from arr2
    while j < m:
        ans.append(arr2[j])
        j += 1
        while j < m and arr2[j] == arr2[j - 1]:
            j += 1
    
    return ans


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3]
    n = 5
    m = 3
    
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    
    result = findUnion(arr1, arr2, n, m)
    
    print("Union:", result)
    # Expected: [1, 2, 3, 4, 5]

# TIME COMPLEXITY = O(N+M) 
