class X { public static void prefixSum2D ( int a [ ] [ ] ) { int R = a . length ; int C = a [ 0 ] . length ; int psa [ ] [ ] = new int [ R ] [ C ] ; psa [ 0 ] [ 0 ] = a [ 0 ] [ 0 ] ; for ( int i = 1 ; i < R ; i ++ ) for ( int j = 1 ; j < C ; j ++ ) psa [ i ] [ j ] = psa [ i - 1 ] [ j ] + psa [ i ] [ j - 1 ] - psa [ i - 1 ] [ j - 1 ] + a [ i ] [ j ] ; for ( int i = 0 ; i < R ; i ++ ) { for ( int j = 0 ; j < C ; j ++ ) System . out . print ( psa [ i ] [ j ] + " ▁ " ) ; System . out . println ( ) ; } }
 }