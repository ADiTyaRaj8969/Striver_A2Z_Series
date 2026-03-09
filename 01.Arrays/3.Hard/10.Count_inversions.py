"""
QUESTION:-
Count inversions in array (pairs where i < j but arr[i] > arr[j]).

Example:
Input: arr = [2, 4, 1, 3, 5]
Output: 3 (inversions: (2,1), (4,1), (4,3))
"""

def countInversions(arr):
    """Count inversions using merge sort. O(N log N) time."""
    def merge_sort_count(arr, left, right):
        if left >= right:
            return 0
        inv_count = 0
        mid = (left + right) // 2
        inv_count += merge_sort_count(arr, left, mid)
        inv_count += merge_sort_count(arr, mid + 1, right)
        inv_count += merge(arr, left, mid, right)
        return inv_count
    
    def merge(arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        inv = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                inv += len(left_arr) - i
                j += 1
            k += 1
        arr[k:] = left_arr[i:] + right_arr[j:]
        return inv
    
    arr_copy = arr.copy()
    return merge_sort_count(arr_copy, 0, len(arr) - 1)

if __name__ == "__main__":
    print("Test 1:", countInversions([2, 4, 1, 3, 5]), "| Expected: 3")
    print("Test 2:", countInversions([2, 3, 4, 5, 6]), "| Expected: 0")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)