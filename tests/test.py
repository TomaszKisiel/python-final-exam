class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test( func, input, output ):
    print(f"{colors.OKBLUE}TEST BEGINING WITH:{colors.ENDC}")
    print("\tINPUT: {}".format(input))
    print("\tCORRECT OUTPUT: {}".format(output))

    result = func(input)
    print("\tFUNCTION RETURNED: {}".format(result))

    if result == output:
        print(f"{colors.OKBLUE}TEST RESULT:{colors.ENDC} {colors.OKGREEN}CORRECT{colors.ENDC}")
    else:
        print(f"{colors.OKBLUE}TEST RESULT:{colors.ENDC} {colors.FAIL}INCORRECT{colors.ENDC}")
    print()