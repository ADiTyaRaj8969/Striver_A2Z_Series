# Traverse the array using loop and when the element is equal to k return the index

# CODE:-
def linearSearch(arr, n, k):
    """Find the index of element k in array"""
    for i in range(n):
        if arr[i] == k:
            return i
    return -1


if __name__ == '__main__':
    arr = [5, 3, 7, 2, 8, 1, 9]
    n = 7
    k = 8
    
    print("Array:", arr)
    
    index = linearSearch(arr, n, k)
    
    if index != -1:
        print(f"Element {k} found at index: {index}")
    else:
        print(f"Element {k} not found")

# TIME COMPLEXITY = O(N) 
