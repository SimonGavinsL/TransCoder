class X { static int countPS ( int i , int j ) { if ( i == j ) return dp [ 1 ] [ j ] = 1 ; else if ( str . charAt ( i ) == str . charAt ( j ) ) return dp [ i ] [ j ] = countPS ( i + 1 , j ) + countPS ( i , j - 1 ) + 1 ; else return dp [ i ] [ j ] = countPS ( i + 1 , j ) + countPS ( i , j - 1 ) - countPS ( i + 1 , j - 1 ) ; }
 }