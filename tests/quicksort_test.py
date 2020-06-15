from quicksort import quicksort as sort

if sort([1,2,6,3,2,5]) == [1,2,2,3,5,6]:
    print ( "TEST: #1 : CORRECT" )
else:
    print ( "TEST: #1 : INCORRECT" )

if sort([20,32,12,69,17,1,-10]) == [-10,1,12,17,20,32,69]:
    print ( "TEST: #2 : CORRECT" )
else:
    print ( "TEST: #2 : INCORRECT" )

if sort([6,7,8,1,2,3,1,2,3,10]) == [1,1,2,2,3,3,6,7,8,10]:
    print ( "TEST: #3 : CORRECT" )
else:
    print ( "TEST: #3 : INCORRECT" )