static int MaximumPath ( int Mat [ ] [ ] ) { int result = 0 ; int dp [ ] [ ] = new int [ N ] [ N + 2 ] ; for ( int i = 0 ; i <= N ; i ++ ) result = Math . max ( result , dp [ N - 1 ] [ i ] ) ; return result ; }
