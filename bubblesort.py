def bubblesort(arr):
    if len(arr) < 2:
        return arr

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if int(arr[i]) < int(arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr
