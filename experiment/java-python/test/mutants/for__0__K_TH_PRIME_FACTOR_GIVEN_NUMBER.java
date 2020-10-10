static int kPrimeFactor ( int n , int k ) { while ( n % 2 == 0 ) { k -- ; n = n / 2 ; if ( k == 0 ) return 2 ; } if ( n > 2 && k == 1 ) return n ; return - 1 ; }
