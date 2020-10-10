class X { static int minCost ( int a [ ] , int n , int k ) { int dp [ ] [ ] = new int [ n + 1 ] [ k + 1 ] ; dp [ 0 ] [ 0 ] = 0 ; return dp [ n ] [ k ] ; }
 }