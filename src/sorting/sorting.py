import iterative_sorting

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # merged_arr = iterative_sorting.selection_sort(arrA + arrB)

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0 # pointer for arrA
    j = 0 # pointer for arrB
    k = 0 # pointer for merged_arr
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

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


merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
