static int numberOfPaths ( int m , int n ) { return numberOfPaths ( m - 1 , n ) + numberOfPaths ( m , n - 1 ) ; }
