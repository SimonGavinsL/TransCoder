class X { static int zigzag ( int n , int k ) { int dp [ ] [ ] = new int [ n + 1 ] [ k + 1 ] ; dp [ 0 ] [ 0 ] = 1 ; return dp [ n ] [ k ] ; }
 }