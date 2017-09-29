# Bubble Sort is the simplest sorting algorithm that works by repeatedly
# swapping the adjacent elements if they are in wrong order.


def bubbleSortR(array, end):
    if (end == 0):
        return
    for i in range(0, end-1):
        if (array[i] > array[i+1]):
            k = array[i]
            array[i] = array[i+1]
            array[i+1] = k
    bubbleSortR(array, end-1)
