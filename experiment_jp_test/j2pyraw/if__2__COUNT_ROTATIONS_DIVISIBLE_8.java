class X { static int countRotationsDivBy8 ( String n ) { int len = n . length ( ) ; int count = 0 ; int threeDigit ; threeDigit = ( n . charAt ( len - 1 ) - '0' ) * 100 + ( n . charAt ( 0 ) - '0' ) * 10 + ( n . charAt ( 1 ) - '0' ) ; threeDigit = ( n . charAt ( len - 2 ) - '0' ) * 100 + ( n . charAt ( len - 1 ) - '0' ) * 10 + ( n . charAt ( 0 ) - '0' ) ; if ( threeDigit % 8 == 0 ) count ++ ; return count ; }
 }