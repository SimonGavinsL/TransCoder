static long answer ( int n ) { int dp [ ] [ ] = new int [ n + 1 ] [ 10 ] ; if ( n == 1 ) return 10 ; long sum = 0 ; for ( int j = 1 ; j <= 9 ; j ++ ) sum += dp [ n ] [ j ] ; return sum ; }
