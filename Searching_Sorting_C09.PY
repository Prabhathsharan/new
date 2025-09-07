def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = [5, 3, 8, 4, 2]
print(linear_search(arr, 8))  # Output: 2



def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search(["apple", "banana", "cherry"], "banana"))  # Output: 1


def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

print(linear_search([10, 20, 30], 25))  # Output: False


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3



def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
"SORTING.PY" 132L, 2999B