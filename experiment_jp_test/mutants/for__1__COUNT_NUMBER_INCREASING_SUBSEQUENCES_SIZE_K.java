static int numOfIncSubseqOfSizeK ( int arr [ ] , int n , int k ) { int dp [ ] [ ] = new int [ k ] [ n ] , sum = 0 ; for ( int i = k - 1 ; i < n ; i ++ ) { sum += dp [ k - 1 ] [ i ] ; } return sum ; }
