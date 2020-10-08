class X { static int minTime ( int n , int k , int a [ ] ) { int temp ; int minTime = 0 ; for ( int i = 0 ; i < n ; i += k ) minTime += ( 2 * a [ i ] ) ; return minTime ; }
 }