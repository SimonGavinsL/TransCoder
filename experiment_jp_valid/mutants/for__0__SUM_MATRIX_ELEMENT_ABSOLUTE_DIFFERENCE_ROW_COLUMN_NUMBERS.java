static int findSum ( int n ) { int [ ] [ ] arr = new int [ n ] [ n ] ; int sum = 0 ; for ( int i = 0 ; i < n ; i ++ ) for ( int j = 0 ; j < n ; j ++ ) sum += arr [ i ] [ j ] ; return sum ; }
