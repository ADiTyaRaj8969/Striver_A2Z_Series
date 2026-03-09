"""
QUESTION:-\nMerge two sorted arrays nums1 and nums2 into nums1 in-place.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""

def merge(nums1, m, nums2, n):
    """Merge two sorted arrays in-place. O(M+N) time, O(1) space."""
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    merge(nums1, 3, [2,5,6], 3)
    print("Test 1:", nums1, "| Expected: [1,2,2,3,5,6]")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)