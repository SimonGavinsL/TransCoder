class X { static int count ( int S [ ] , int m , int n ) { if ( m <= 0 && n >= 1 ) return 0 ; return count ( S , m - 1 , n ) + count ( S , m , n - S [ m - 1 ] ) ; }
 }