static int count ( int n ) { int rem = n % 4 ; if ( rem == 3 ) { if ( n < 15 ) return - 1 ; return ( n - 15 ) / 4 + 2 ; } return 0 ; }
