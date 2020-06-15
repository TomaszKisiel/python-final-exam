from tests.test import test
from is_prime import is_prime

test( is_prime, [ 7 ], True )
test( is_prime, [ 2 ], True )
test( is_prime, [ 6 ], False )
test( is_prime, [ 47 ], True )
test( is_prime, [ 46 ], False )
test( is_prime, [ 89 ], True )
test( is_prime, [ 97 ], True )
test( is_prime, [ 16 ], False )