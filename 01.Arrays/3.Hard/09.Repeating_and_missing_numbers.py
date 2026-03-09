"""
QUESTION:-\nFind the repeating and missing numbers in array of 1 to N.

Example:
Input: arr = [2, 2]
Output: [2, 1] (repeating=2, missing=1)
"""

def findTwoElement(arr):
    \"\"\"Find repeating and missing numbers. O(N) time, O(1) space.\"\"\"
    n = len(arr)
    opt_sum = n * (n + 1) // 2
    opt_sum_sq = n * (n + 1) * (2 * n + 1) // 6
    
    actual_sum = sum(arr)
    actual_sum_sq = sum(x * x for x in arr)
    
    x_minus_y = opt_sum - actual_sum
    x_plus_y = (opt_sum_sq - actual_sum_sq) // x_minus_y
    
    x = (x_plus_y + x_minus_y) // 2
    y = x_plus_y - x
    
    return [y, x]

if __name__ == "__main__":
    print("Test 1:", findTwoElement([2, 2]), "| Expected: [2, 1]")
    print("Test 2:", findTwoElement([1, 3, 3, 4]), "| Expected: [3, 2]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)