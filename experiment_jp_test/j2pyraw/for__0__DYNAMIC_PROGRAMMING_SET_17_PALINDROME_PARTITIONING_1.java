class X { static int minPalPartion ( String str ) { int n = str . length ( ) ; int [ ] C = new int [ n ] ; boolean [ ] [ ] P = new boolean [ n ] [ n ] ; int i , j , k , L ; for ( L = 2 ; L <= n ; L ++ ) { for ( i = 0 ; i < n - L + 1 ; i ++ ) { j = i + L - 1 ; if ( L == 2 ) P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) ; else P [ i ] [ j ] = ( str . charAt ( i ) == str . charAt ( j ) ) && P [ i + 1 ] [ j - 1 ] ; } } for ( i = 0 ; i < n ; i ++ ) { if ( P [ 0 ] [ i ] == true ) C [ i ] = 0 ; else { C [ i ] = Integer . MAX_VALUE ; for ( j = 0 ; j < i ; j ++ ) { if ( P [ j + 1 ] [ i ] == true && 1 + C [ j ] < C [ i ] ) C [ i ] = 1 + C [ j ] ; } } } return C [ n - 1 ] ; }
 }