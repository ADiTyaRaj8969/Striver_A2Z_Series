# QUESTION:-
# Given an array A[] of size n, find the largest element in it.
# Example: Input: n = 5, A[] = {1, 8, 7, 56, 90}, Output: 90

# APPROACH:-
# Initialize ans with the first element
# Traverse the entire array and update ans if element is greater
# Finally, return ans

# CODE:-
def largest(arr, n):
    """Find the largest element in array"""
    ans = arr[0]
    for i in range(1, n):
        if arr[i] > ans:
            ans = arr[i]
    return ans


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    n1 = 5
    arr1 = [1, 8, 7, 56, 90]
    result1 = largest(arr1, n1)
    print(f"Output: {result1}")
    print(f"Expected: 90")

# TIME COMPLEXITY = O(N) 
