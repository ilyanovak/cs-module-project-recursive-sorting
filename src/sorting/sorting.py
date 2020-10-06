import iterative_sorting

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    merged_arr = iterative_sorting.selection_sort(arrA + arrB)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if arr == []:
        return []
    # if array is size is one then return the array
    if len(arr) == 1:
        return arr
    # if the array size is great than 1 then split array and run merge_sort on them
    middle = len(arr) // 2
    arrA = merge_sort(arr[:middle])
    arrB = merge_sort(arr[middle:])
    return merge(arrA, arrB)


arr1 = [8, 1, 5]
merge_sort(arr1)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
