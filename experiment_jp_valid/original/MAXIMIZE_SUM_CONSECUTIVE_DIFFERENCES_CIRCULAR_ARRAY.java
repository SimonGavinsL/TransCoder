static int maxSum ( int arr [ ] , int n ) { int sum = 0 ; Arrays . sort ( arr ) ; for ( int i = 0 ; i < n / 2 ; i ++ ) { sum -= ( 2 * arr [ i ] ) ; sum += ( 2 * arr [ n - i - 1 ] ) ; } return sum ; }
