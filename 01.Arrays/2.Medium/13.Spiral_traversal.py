"""
QUESTION:-
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# APPROACH:-
# Use four boundaries: top, bottom, left, right
# Traverse in spiral order:
# 1. Left to right on top row
# 2. Top to bottom on right column
# 3. Right to left on bottom row (if row exists)
# 4. Bottom to top on left column (if column exists)
# Shrink boundaries after each traversal

# CODE:-

def spiralOrder(matrix):
    """
    Return all elements of matrix in spiral order.
    
    Time Complexity: O(M * N)
    Space Complexity: O(1) (excluding output array)
    """
    if not matrix or not matrix[0]:
        return []
    
    m = len(matrix)
    n = len(matrix[0])
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    ans = []
    
    while top <= bottom and left <= right:
        # Traverse top row from left to right
        for j in range(left, right + 1):
            ans.append(matrix[top][j])
        top += 1
        
        # Traverse right column from top to bottom
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1
        
        # Traverse bottom row from right to left (if row exists)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1
        
        # Traverse left column from bottom to top (if column exists)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
    
    return ans


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = spiralOrder(matrix1)
    print(f"Input: {matrix1}")
    print(f"Output: {result1}")
    print(f"Expected: [1,2,3,6,9,8,7,4,5]")
    print()

    # Test case 2
    print("Test 2:")
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result2 = spiralOrder(matrix2)
    print(f"Input: {matrix2}")
    print(f"Output: {result2}")
    print(f"Expected: [1,2,3,4,8,12,11,10,9,5,6,7]")
    print()

    # Test case 3
    print("Test 3:")
    matrix3 = [[1, 2, 3]]
    result3 = spiralOrder(matrix3)
    print(f"Input: {matrix3}")
    print(f"Output: {result3}")
    print(f"Expected: [1,2,3]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(H)