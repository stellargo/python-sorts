# Sort an arr[] of size n
# Loop from i = 1 to n-1.
# Pick element arr[i] and insert it into sorted sequence arr[0…i-1]


def insertionSort(array):
    for toputinplace in range(1, len(array)):
        for traverse in range(toputinplace):
            if array[traverse] > array[toputinplace]:
                temp = array[toputinplace]
                for k in range(toputinplace, traverse, -1):
                    array[k] = array[k-1]
                array[traverse] = temp
