"""
QUESTION:-
Find the subarray with the largest product.

Example:
Input: nums = [2, 3, -2, 4]
Output: 6 (subarray [2, 3])
"""

def maxProduct(nums):
    """Find max product subarray. O(N) time, O(1) space."""
    if not nums:
        return 0
    max_prod = float('-inf')
    product = 1
    
    for num in nums:
        product *= num
        max_prod = max(max_prod, product)
        if product == 0:
            product = 1
    
    product = 1
    for num in reversed(nums):
        product *= num
        max_prod = max(max_prod, product)
        if product == 0:
            product = 1
    
    return max_prod

if __name__ == "__main__":
    print("Test 1:", maxProduct([2, 3, -2, 4]), "| Expected: 6")
    print("Test 2:", maxProduct([-2]), "| Expected: -2")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)