static int maxProd ( int n ) { int res = 1 ; while ( n > 4 ) { n -= 3 ; res *= 3 ; } return ( n * res ) ; }
