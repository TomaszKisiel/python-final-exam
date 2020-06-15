def generate( length ):
    prev = 1
    sum = 1

    if length < 1:
        return []
    elif length == 1:
        return [1]

    arr = [prev, sum]
    for i in range(0, length - 2):
        temp = sum
        sum += prev
        prev = temp
        arr.append(sum)

    return arr



