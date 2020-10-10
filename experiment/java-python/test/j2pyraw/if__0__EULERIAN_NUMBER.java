class X { public static int eulerian ( int n , int m ) { if ( m == 0 ) return 1 ; return ( n - m ) * eulerian ( n - 1 , m - 1 ) + ( m + 1 ) * eulerian ( n - 1 , m ) ; }
 }