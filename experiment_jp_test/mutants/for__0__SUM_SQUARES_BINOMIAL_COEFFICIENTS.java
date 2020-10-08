static int sumofsquare ( int n ) { int [ ] [ ] C = new int [ n + 1 ] [ n + 1 ] ; int i , j ; int sum = 0 ; for ( i = 0 ; i <= n ; i ++ ) sum += ( C [ n ] [ i ] * C [ n ] [ i ] ) ; return sum ; }
