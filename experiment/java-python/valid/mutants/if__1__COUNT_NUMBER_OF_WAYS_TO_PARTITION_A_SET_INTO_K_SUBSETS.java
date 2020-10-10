public static int countP ( int n , int k ) { return ( k * countP ( n - 1 , k ) + countP ( n - 1 , k - 1 ) ) ; }
