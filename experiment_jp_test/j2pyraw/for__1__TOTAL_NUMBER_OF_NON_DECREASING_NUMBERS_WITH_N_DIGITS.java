class X { static int countNonDecreasing ( int n ) { int dp [ ] [ ] = new int [ 10 ] [ n + 1 ] ; int count = 0 ; for ( int i = 0 ; i < 10 ; i ++ ) count += dp [ i ] [ n ] ; return count ; }
 }