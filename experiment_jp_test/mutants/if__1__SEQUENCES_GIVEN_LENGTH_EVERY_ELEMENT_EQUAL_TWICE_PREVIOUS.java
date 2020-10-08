static int getTotalNumberOfSequences ( int m , int n ) { return getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m / 2 , n - 1 ) ; }
