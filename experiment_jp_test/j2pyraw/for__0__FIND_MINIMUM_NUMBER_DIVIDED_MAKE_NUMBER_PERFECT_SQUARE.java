class X { static int findMinNumber ( int n ) { int count = 0 , ans = 1 ; while ( n % 2 == 0 ) { count ++ ; n /= 2 ; } if ( count % 2 == 1 ) ans *= 2 ; if ( n > 2 ) ans *= n ; return ans ; }
 }