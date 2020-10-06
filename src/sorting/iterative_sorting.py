# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for start_item in range(0, len(arr)-1):
        small_item = start_item
        for curr_item in range(start_item, len(arr)):
            if arr[curr_item] < arr[small_item]: small_item = curr_item
        arr[start_item], arr[small_item] = arr[small_item], arr[start_item]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # end of list element starts at last element and iterates to second element
    for end_of_list in reversed(range(1, len(arr))):
        # current item starts at first element and iterates to end of list element
        for curr_item in range(end_of_list):
            # next item is set to element that follows current item
            next_item = curr_item + 1
            # if value at current item is greater than value ext next element
            if arr[curr_item] > arr[next_item]:
                # switch current item and next item values
                arr[curr_item], arr[next_item] = arr[next_item], arr[curr_item]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
