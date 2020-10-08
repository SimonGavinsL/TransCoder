static int countWays ( int n ) { int DP [ ] = new int [ n + 1 ] ; DP [ 0 ] = DP [ 1 ] = DP [ 2 ] = 1 ; DP [ 3 ] = 2 ; return DP [ n ] ; }
