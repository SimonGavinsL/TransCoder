static int lastPosition ( int n , int m , int k ) { m = m - ( n - k + 1 ) ; return ( m % n == 0 ) ? n : ( m % n ) ; }
