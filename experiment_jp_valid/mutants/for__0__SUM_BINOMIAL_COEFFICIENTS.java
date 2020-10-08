static int binomialCoeffSum ( int n ) { int C [ ] [ ] = new int [ n + 1 ] [ n + 1 ] ; int sum = 0 ; for ( int i = 0 ; i <= n ; i ++ ) sum += C [ n ] [ i ] ; return sum ; }
