"""
QUESTION:-
Given an integer rowIndex, return the rowIndex-th (0-indexed) row of Pascal's triangle.

Example:
Input: rowIndex = 3
Output: [1, 3, 3, 1]
"""

def getRow(rowIndex):
    """Get the rowIndex-th row of Pascal's triangle."""
    row = [1] * (rowIndex + 1)
    coefficient = 1
    for col in range(1, rowIndex + 1):
        coefficient = coefficient * (rowIndex - col + 1) // col
        row[col] = coefficient
    return row

if __name__ == "__main__":
    print("Test 1:", getRow(3), "| Expected: [1, 3, 3, 1]")
    print("Test 2:", getRow(0), "| Expected: [1]")

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)