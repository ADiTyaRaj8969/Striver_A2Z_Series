# CODE:-
# RIGHT ROATATE:-
# to keep k within the range
# LEFT ROATATE:-
# to keep k within the range
# Test case 1
# Test case 2
# TIME COMPLEXITY = O(N)

def rightRotate(arr, n, k):
    """
    Rotate array right by k positions
    Approach: Reverse (n-k) elements, then k elements, then all
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n == 0:
        return arr
    k = k % n  # handle k > n
    # Reverse first (n-k) elements
    arr[:n-k] = arr[:n-k][::-1]
    # Reverse last k elements
    arr[n-k:] = arr[n-k:][::-1]
    # Reverse entire array
    arr[:] = arr[::-1]
    return arr


def leftRotate(arr, n, k):
    """
    Rotate array left by k positions
    Approach: Reverse k elements, then (n-k) elements, then all
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n == 0:
        return arr
    k = k % n  # handle k > n
    # Reverse first k elements
    arr[:k] = arr[:k][::-1]
    # Reverse remaining (n-k) elements
    arr[k:] = arr[k:][::-1]
    # Reverse entire array
    arr[:] = arr[::-1]
    return arr


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original:", nums)
    result = rightRotate(nums.copy(), len(nums), k)
    print(f"After right rotating by {k}:", result)
    # Expected: [5, 6, 7, 1, 2, 3, 4]

# TIME COMPLEXITY = O(N) 
