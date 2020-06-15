def quicksort( arr ):
    pivot = len( arr )

    if pivot < 2:
        return arr

    current_position = 0

    for i in range(1, pivot):
        if int(arr[i]) <= int(arr[0]):
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp

    left = quicksort( arr[0:current_position] )
    right = quicksort( arr[current_position+1:pivot])

    arr = left + [arr[current_position]] + right

    return arr
