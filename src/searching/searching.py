# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if array is empty
    if arr == []:
        return - 1
    # calculate average as halfway in between start and end
    average = end // 2
    # if target is found in the array
    if arr[average] == target:
        return average
    # if the target is not found in the array
    if start >= end:
        return -1  # not found
    # if the target is to the left of the average
    if arr[average] > target:
        return binary_search(arr, target, start, average)
    # otherwise if the target is the right of the average
    else:
        return binary_search(arr, target, average, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
