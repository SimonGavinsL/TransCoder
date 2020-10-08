class X { static int getTotalNumberOfSequences ( int m , int n ) { if ( n == 0 ) return 1 ; return getTotalNumberOfSequences ( m - 1 , n ) + getTotalNumberOfSequences ( m / 2 , n - 1 ) ; }
 }