"""
QUESTION:-
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's in-place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

# APPROACH:-
# Use first row and first column as markers for zeros.
# 1. Check if first row and column originally contain zeros
# 2. Mark zeros in first row/column for cells that have zero
# 3. Use marked cells to set rows and columns to zero
# 4. Handle first row and column separately based on initial state

# CODE:-

def setZeroes(matrix):
    """
    Set entire row and column to 0 if element is 0. Works in-place.
    
    Time Complexity: O(M * N)
    Space Complexity: O(1)
    """
    m = len(matrix)
    n = len(matrix[0])
    
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row contains zero
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    # Check if first column contains zero
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # Mark zeros in first row and column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set rows to zero
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
    
    # Set columns to zero
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
    
    # Set first row to zero if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    # Set first column to zero if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix1)
    print(f"Output: {matrix1}")
    print(f"Expected: [[1,0,1],[0,0,0],[1,0,1]]")
    print()

    # Test case 2
    print("Test 2:")
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(matrix2)
    print(f"Output: {matrix2}")
    print(f"Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]")
    print()

    # Test case 3
    print("Test 3:")
    matrix3 = [[1, 2], [0, 3]]
    setZeroes(matrix3)
    print(f"Output: {matrix3}")
    print(f"Expected: [[0,2],[0,0]]")

# TIME COMPLEXITY = O(M * N)
# SPACE COMPLEXITY = O(1)
