class X { static int count ( String a , String b ) { int m = a . length ( ) ; int n = b . length ( ) ; int lookup [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ; for ( int i = 1 ; i <= m ; i ++ ) { for ( int j = 1 ; j <= n ; j ++ ) { if ( a . charAt ( i - 1 ) == b . charAt ( j - 1 ) ) lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ] ; else lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ] ; } } return lookup [ m ] [ n ] ; }
 }