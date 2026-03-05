# CODE:-
# TIME COMPLEXITY = O(N)

def rotateArray(arr, n):
    """
    Rotate array left by 1 position
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n == 0:
        return arr
    
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = 5
    print("Original array:", arr)
    rotateArray(arr, n)
    print("After rotating left by 1:", arr)
    # Expected: [2, 3, 4, 5, 1] 
