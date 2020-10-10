class X { static int numberofways ( int n , int m ) { int dp [ ] [ ] = new int [ n + 2 ] [ n + 2 ] ; dp [ 0 ] [ n + 1 ] = 1 ; return dp [ n ] [ m ] ; }
 }