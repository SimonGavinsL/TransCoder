public static int maxCost ( int mat [ ] [ ] , int N ) { int dp [ ] [ ] = new int [ N ] [ N ] ; dp [ 0 ] [ 0 ] = mat [ 0 ] [ 0 ] ; int result = 0 ; for ( int i = 0 ; i < N ; i ++ ) if ( result < dp [ N - 1 ] [ i ] ) result = dp [ N - 1 ] [ i ] ; return result ; }
