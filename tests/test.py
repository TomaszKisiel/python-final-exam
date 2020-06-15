def test( func, input, output ):
    print("TEST BEGINING WITH:")
    print("\tINPUT: {}".format(input))
    print("\tCORRECT OUTPUT: {}".format(output))

    result = func(input)
    print("\tFUNCTION RETURNED: {}".format(result))

    if result == output:
        print("TEST RESULT: CORRECT")
    else:
        print("TEST RESULT: INCORRECT")
    print()