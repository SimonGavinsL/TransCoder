class X { static int shortestSeq ( char [ ] S , char [ ] T ) { int m = S . length , n = T . length ; int dp [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ; for ( int i = 1 ; i <= m ; i ++ ) { for ( int j = 1 ; j <= n ; j ++ ) { char ch = S [ i - 1 ] ; int k ; for ( k = j - 1 ; k >= 0 ; k -- ) { if ( T [ k ] == ch ) { break ; } } if ( k == - 1 ) { dp [ i ] [ j ] = 1 ; } else { dp [ i ] [ j ] = Math . min ( dp [ i - 1 ] [ j ] , dp [ i - 1 ] [ k ] + 1 ) ; } } } int ans = dp [ m ] [ n ] ; if ( ans >= MAX ) { ans = - 1 ; } return ans ; }
 }