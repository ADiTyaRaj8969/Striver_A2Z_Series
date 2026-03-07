"""
QUESTION:-
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees clockwise.
Must solve it in-place.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

# APPROACH:-
# 1. Transpose the matrix: swap elements (i,j) with (j,i)
# 2. Reverse each row
# This achieves a 90-degree clockwise rotation

# CODE:-

def rotate(matrix):
    """
    Rotate matrix 90 degrees clockwise in-place.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i):
            # Swap matrix[i][j] and matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test 1:")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix1)
    print(f"Output: {matrix1}")
    print(f"Expected: [[7,4,1],[8,5,2],[9,6,3]]")
    print()

    # Test case 2
    print("Test 2:")
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix2)
    print(f"Output: {matrix2}")
    print(f"Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]")
    print()

    # Test case 3
    print("Test 3:")
    matrix3 = [[1]]
    rotate(matrix3)
    print(f"Output: {matrix3}")
    print(f"Expected: [[1]]")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)