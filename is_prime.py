import math

def is_prime( num ):
    if num == 2:
        return True

    for i in range ( 2, math.ceil( num**0.5 ) + 1 ):
        if num % i == 0:
            return False

    return True