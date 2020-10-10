static long countWays ( int n ) { long dp [ ] [ ] = new long [ 2 ] [ n + 1 ] ; dp [ 0 ] [ 1 ] = 1 ; dp [ 1 ] [ 1 ] = 2 ; return dp [ 0 ] [ n ] + dp [ 1 ] [ n ] ; }
