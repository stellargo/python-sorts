# Bubble Sort is the simplest sorting algorithm that works by repeatedly
# swapping the adjacent elements if they are in wrong order.

#best case time complexity: 0(n)
def bubbleSort(array):
    for j in range(len(array)):
        #array is assumed to be sorted by setting flag = 1
        flag = 1
        for i in range(len(array)-1-j):
            if array[i] > array[i+1]:
                #array is not sorted
                flag = 0
                #swapping 
                array[i],array[i+1] = array[i+1],array[i]
        #if no swap is done in previous pass, then return i.e. array is already sorted
        if flag == 1:
            return 
