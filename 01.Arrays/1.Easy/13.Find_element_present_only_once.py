# QUESTION:-
# Find the single number that appears once (all others appear twice)
# Example 1: Input: [2,2,1], Output: 1
# Example 2: Input: [4,1,2,1,2], Output: 4

# APPROACH:-
# Use XOR operation: XOR of two same numbers is 0, XOR of 0 with any number gives that number
# XOR all elements - pairs will cancel out and we'll be left with the single number

# CODE:-
def singleNumber(nums):
    """Use XOR - same elements cancel out"""
    xr = 0
    for i in range(len(nums)):
        xr = nums[i] ^ xr
    return xr


if __name__ == '__main__':
    print(singleNumber([2, 2, 1]))  # Output: 1
    print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
