class X { static int waysToIncreaseLCSBy1 ( String str1 , String str2 ) { int m = str1 . length ( ) , n = str2 . length ( ) ; Vector < Integer > [ ] position = new Vector [ M ] ; int [ ] [ ] lcsl = new int [ m + 2 ] [ n + 2 ] ; int [ ] [ ] lcsr = new int [ m + 2 ] [ n + 2 ] ; int ways = 0 ; for ( int i = 0 ; i <= m ; i ++ ) { for ( char d = 0 ; d < 26 ; d ++ ) { for ( int j = 0 ; j < position [ d ] . size ( ) ; j ++ ) { int p = position [ d ] . elementAt ( j ) ; if ( lcsl [ i ] [ p - 1 ] + lcsr [ i + 1 ] [ p + 1 ] == lcsl [ m ] [ n ] ) ways ++ ; } } } return ways ; }
 }