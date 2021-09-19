arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # O(n)
arr[3] = 4  # O(1)

# Reverse
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # O(n)
i = len(arr)-1
new_array = arr[::-1]

"""
Ques - Replace each even number in an array with two of the same number.
e.g [1, 2, 5, 6, 8] -> [1, 2, 2, 5, 6, 6, 8, 8].
Assume that the array has enough space to accommodate the result.

1, 2, 5, 6, 8, -1, -1, -1 = i
"""


def replaceEven(arr):
    if not arr:
        return arr
    right = len(arr)-1
    i = len(arr)-1
    while i >= 0 and arr[i] == -1:
        i -= 1
    while i >= 0:
        if arr[i] % 2 == 0:
            arr[right] = arr[i]
            right -= 1
        arr[right] = arr[i]
        right -= 1
        i -= 1
    return arr
