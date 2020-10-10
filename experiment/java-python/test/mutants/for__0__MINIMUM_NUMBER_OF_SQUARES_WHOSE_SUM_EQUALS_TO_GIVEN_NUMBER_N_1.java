static int getMinSquares ( int n ) { if ( n <= 3 ) return n ; int dp [ ] = new int [ n + 1 ] ; dp [ 0 ] = 0 ; dp [ 1 ] = 1 ; dp [ 2 ] = 2 ; dp [ 3 ] = 3 ; int res = dp [ n ] ; return res ; }
