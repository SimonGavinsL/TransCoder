public static int countP ( int n , int k ) { if ( k == 1 || k == n ) return 1 ; return ( k * countP ( n - 1 , k ) + countP ( n - 1 , k - 1 ) ) ; }
