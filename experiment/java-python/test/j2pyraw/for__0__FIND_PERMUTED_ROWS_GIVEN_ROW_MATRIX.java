class X { static void permutatedRows ( int mat [ ] [ ] , int m , int n , int r ) { LinkedHashSet < Integer > s = new LinkedHashSet < > ( ) ; for ( int i = 0 ; i < m ; i ++ ) { if ( i == r ) continue ; int j ; for ( j = 0 ; j < n ; j ++ ) if ( ! s . contains ( mat [ i ] [ j ] ) ) break ; if ( j != n ) continue ; System . out . print ( i + " , ▁ " ) ; } }
 }