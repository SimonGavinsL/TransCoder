static int findLargestPlus ( int mat [ ] [ ] ) { int left [ ] [ ] = new int [ N ] [ N ] ; int right [ ] [ ] = new int [ N ] [ N ] ; int top [ ] [ ] = new int [ N ] [ N ] ; int bottom [ ] [ ] = new int [ N ] [ N ] ; int n = 0 ; for ( int i = 0 ; i < N ; i ++ ) { for ( int j = 0 ; j < N ; j ++ ) { int len = Math . min ( Math . min ( top [ i ] [ j ] , bottom [ i ] [ j ] ) , Math . min ( left [ i ] [ j ] , right [ i ] [ j ] ) ) ; if ( len > n ) n = len ; } } if ( n > 0 ) return 4 * ( n - 1 ) + 1 ; return 0 ; }
