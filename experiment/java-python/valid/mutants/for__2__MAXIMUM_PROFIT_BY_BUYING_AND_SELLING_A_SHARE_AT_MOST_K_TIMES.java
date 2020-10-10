static int maxProfit ( int [ ] price , int n , int k ) { int [ ] [ ] profit = new int [ k + 1 ] [ n + 1 ] ; return profit [ k ] [ n - 1 ] ; }
