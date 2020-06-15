from tests.test import test
from quicksort import quicksort as sort

test( sort, [1,2,6,3,2,5], [1,2,2,3,5,6])
test( sort, [20,32,12,69,17,1,-10], [-10,1,12,17,20,32,69])
test( sort, [6,7,8,1,2,3,1,2,3,10], [1,1,2,4,2,3,3,6,7,8,10])