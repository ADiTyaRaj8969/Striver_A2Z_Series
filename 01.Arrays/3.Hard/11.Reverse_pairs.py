"""
QUESTION:-
Count reverse pairs where i < j and nums[i] > 2 * nums[j].

Example:
Input: nums = [1, 3, 2, 3, 1]
Output: 2 (pairs: (1,4) and (3,4))
"""

def reversePairs(nums):
    """Count reverse pairs using merge sort. O(N log N) time."""
    def merge_sort_count(arr, left, right):
        if left >= right:
            return 0
        pair_count = 0
        mid = (left + right) // 2
        pair_count += merge_sort_count(arr, left, mid)
        pair_count += merge_sort_count(arr, mid + 1, right)
        pair_count += merge(arr, left, mid, right)
        return pair_count
    
    def merge(arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        pairs = 0
        j = 0
        for i in range(len(left_arr)):
            while j < len(right_arr) and left_arr[i] > 2 * right_arr[j]:
                j += 1
            pairs += j
        i = j_merge = 0
        k = left
        while i < len(left_arr) and j_merge < len(right_arr):
            if left_arr[i] <= right_arr[j_merge]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j_merge]
                j_merge += 1
            k += 1
        arr[k:] = left_arr[i:] + right_arr[j_merge:]
        return pairs
    
    arr_copy = nums.copy()
    return merge_sort_count(arr_copy, 0, len(nums) - 1)

if __name__ == "__main__":
    print("Test 1:", reversePairs([1, 3, 2, 3, 1]), "| Expected: 2")
    print("Test 2:", reversePairs([2, 4, 3, 5, 1]), "| Expected: 3")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)