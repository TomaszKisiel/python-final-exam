def is_palindrome( str1 ):
    str1 = str1.replace(" ", "")
    str2 = str1[::-1]

    if str1 == str2:
        return True

    return False