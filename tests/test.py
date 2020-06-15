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
    prompt = ">"

    print()
    print(f"{prompt} {colors.OKBLUE}TEST BEGINING WITH:{colors.ENDC}")
    print(f"{prompt}   INPUT: {input}")
    print(f"{prompt}   CORRECT OUTPUT: {output}")

    result = func( *input )
    print(f"{prompt}   FUNCTION RETURNED: {result}")

    if result == output:
        print(f"{prompt} {colors.OKBLUE}TEST RESULT:{colors.ENDC} {colors.OKGREEN}CORRECT{colors.ENDC}")
    else:
        print(f"{prompt} {colors.OKBLUE}TEST RESULT:{colors.ENDC} {colors.FAIL}INCORRECT{colors.ENDC}")
    print()