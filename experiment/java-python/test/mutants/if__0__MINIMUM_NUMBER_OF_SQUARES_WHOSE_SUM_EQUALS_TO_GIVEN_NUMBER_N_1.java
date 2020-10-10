static int getMinSquares ( int n ) { int dp [ ] = new int [ n + 1 ] ; dp [ 0 ] = 0 ; dp [ 1 ] = 1 ; dp [ 2 ] = 2 ; dp [ 3 ] = 3 ; int res = dp [ n ] ; return res ; }
