static int countRotations ( String n ) { int len = n . length ( ) ; int twoDigit , count = 0 ; twoDigit = ( n . charAt ( len - 1 ) - '0' ) * 10 + ( n . charAt ( 0 ) - '0' ) ; return count ; }
