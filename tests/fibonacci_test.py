from tests.test import test
from fibonacci import generate

test( generate, 5, [1,1,2,3,5] )
test( generate, 10, [1,1,2,3,5,8,13,21,34,55] )
test( generate, 12, [1,1,2,3,5,8,13,21,34,55,89,144] )

# print(generate( 2 ))

# if generate( 5 ) == [1,1,2,3,5]:
#     print("TEST: #1 : CORRECT")
# else:
#     print("TEST: #1 : INCORRECT")