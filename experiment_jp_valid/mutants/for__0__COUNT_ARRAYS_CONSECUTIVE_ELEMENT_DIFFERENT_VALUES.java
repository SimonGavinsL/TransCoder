public static int countarray ( int n , int k , int x ) { int [ ] dp = new int [ 109 ] ; dp [ 0 ] = 0 ; dp [ 1 ] = 1 ; return ( x == 1 ? ( k - 1 ) * dp [ n - 2 ] : dp [ n - 1 ] ) ; }
