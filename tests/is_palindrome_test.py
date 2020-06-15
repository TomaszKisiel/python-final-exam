from tests.test import test
from is_palindrome import is_palindrome

test( is_palindrome, ['zakaz'], True )
test( is_palindrome, ['madam'], True )
test( is_palindrome, ['do geese see god'], True )
test( is_palindrome, ['i like bananas'], False )
test( is_palindrome, ['malayalam'], True )
