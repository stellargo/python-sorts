# Sort an arr[] of size n
# Loop from i = 1 to n-1.
# Pick element arr[i] and insert it into sorted sequence arr[0…i-1]


def insertionSortR(array, n):
    if (n == len(array)):
        return
    for traverse in range(n):
        if array[traverse] > array[n]:
            temp = array[n]
            for k in range(n, traverse, -1):
                array[k] = array[k-1]
            array[traverse] = temp
    insertionSortR(array, n+1)
