class X { static long countStrs ( int n ) { long [ ] [ ] dp = new long [ n + 1 ] [ 27 ] ; for ( int i = 2 ; i <= n ; i ++ ) { for ( int j = 0 ; j <= 25 ; j ++ ) { if ( j == 0 ) { dp [ i ] [ j ] = dp [ i - 1 ] [ j + 1 ] ; } else { dp [ i ] [ j ] = ( dp [ i - 1 ] [ j - 1 ] + dp [ i - 1 ] [ j + 1 ] ) ; } } } long sum = 0 ; for ( int i = 0 ; i <= 25 ; i ++ ) { sum = ( sum + dp [ n ] [ i ] ) ; } return sum ; }
 }