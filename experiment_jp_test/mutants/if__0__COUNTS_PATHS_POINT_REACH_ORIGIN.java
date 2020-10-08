static int countPaths ( int n , int m ) { return ( countPaths ( n - 1 , m ) + countPaths ( n , m - 1 ) ) ; }
