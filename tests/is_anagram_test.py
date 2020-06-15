from tests.test import test
from is_anagram import is_anagram

test( is_anagram, [ "żółw", "włóż" ], True )
test( is_anagram, [ "abcde", "ebcda" ], True )
test( is_anagram, [ "magda", "gada" ], False )
test( is_anagram, [ "listen", "silent" ], True )
