# QUESTION:-
# Given an array Arr of size N, print second largest distinct element from an array.
# Example: Input: N = 6, Arr[] = {12, 35, 1, 10, 34, 1}, Output: 34

# APPROACH:-
# If current element is larger than 'large' then update second_large and large
# Else if current element is larger than 'second_large' then update second_large
# Once we traverse entire array, second_large contains the answer

# CODE:-
def print2largest(arr, n):
    """Find the second largest distinct element"""
    prev = -1
    curr = arr[0]
    for i in range(1, n):
        if arr[i] > curr:
            prev = curr
            curr = arr[i]
        elif arr[i] > prev and arr[i] != curr:
            prev = arr[i]
    return prev


if __name__ == '__main__':
    # Test case 1
    print("Test 1:")
    N1 = 6
    arr1 = [12, 35, 1, 10, 34, 1]
    result1 = print2largest(arr1, N1)
    print(f"Output: {result1}")
    print(f"Expected: 34")

# TIME COMPLEXITY = O(N) 
