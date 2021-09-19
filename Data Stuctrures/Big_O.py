"""
- Most Common
- Performance
- Time & Space
- 
"""


def print_array(array):
    print('Enter')  # O(1)
    for i in range(len(array)):  # O(n - 1)
        print(i)  # O(1)
        print(array[i])  # O(1) -> O(n)
    print('Exit')  # O(1)


"""
O(2) + O(2*n) -> O(2 + 2*n) -> O(n)
"""


def printNested(array):
    print('Enter')  # O(1)
    for i in range(len(array)):  # O(n)
        for j in range(len(array[0])):  # O(n)
            print(i, j)  # O(1)
            print(array[i][j])  # O(1) -> O(n*n)
    print('Exit')  # O(1)


"""
-> O(2) + O(n*n * 2) -> O(2 + n2 * 2) -> O(n2)
"""

# Worst Case


def findTarget(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

# 1, 2, 3, 4, 5, 6, 7, 8, O(3), O(7)


# Space Complexity
# a = 1 -> O(1)

def reverse(arr):
    res = [0]*len(arr)
    for i in range(len(arr)):
        res[len(arr)-i-1] = arr[i]
    return res
