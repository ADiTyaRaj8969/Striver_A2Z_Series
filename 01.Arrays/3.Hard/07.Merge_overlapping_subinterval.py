"""
QUESTION:-
Merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

def merge(intervals):
    """Merge overlapping intervals. O(N log N) time."""
    if not intervals:
        return []
    intervals.sort()
    ans = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        else:
            ans.append(intervals[i])
    
    return ans

if __name__ == "__main__":
    print("Test 1:", merge([[1,3],[2,6],[8,10],[15,18]]))
    print("Expected: [[1,6],[8,10],[15,18]]")

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)