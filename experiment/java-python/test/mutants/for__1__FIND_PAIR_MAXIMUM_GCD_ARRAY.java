public static int findMaxGCD ( int arr [ ] , int n ) { int high = 0 ; int divisors [ ] = new int [ high + 1 ] ; for ( int i = high ; i >= 1 ; i -- ) if ( divisors [ i ] > 1 ) return i ; return 1 ; }
