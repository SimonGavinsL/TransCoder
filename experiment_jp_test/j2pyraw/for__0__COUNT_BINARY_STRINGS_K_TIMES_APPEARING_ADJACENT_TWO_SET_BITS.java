class X { static int countStrings ( int n , int k ) { int dp [ ] [ ] [ ] = new int [ n + 1 ] [ k + 1 ] [ 2 ] ; dp [ 1 ] [ 0 ] [ 0 ] = 1 ; dp [ 1 ] [ 0 ] [ 1 ] = 1 ; return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ] ; }
 }