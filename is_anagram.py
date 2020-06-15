def is_anagram( str1, str2 ):
    if str1 == str2:
        return True

    if sorted(str1) == sorted(str2):
        return True

    return False
