static boolean check ( String str ) { int n = str . length ( ) ; if ( ( str . charAt ( n - 1 ) - '0' ) % 2 != 0 ) return false ; int digitSum = 0 ; return ( digitSum % 3 == 0 ) ; }
