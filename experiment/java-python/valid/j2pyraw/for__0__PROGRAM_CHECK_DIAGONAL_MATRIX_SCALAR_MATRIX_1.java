class X { static boolean isScalarMatrix ( int mat [ ] [ ] ) { for ( int i = 0 ; i < N - 1 ; i ++ ) if ( mat [ i ] [ i ] != mat [ i + 1 ] [ i + 1 ] ) return false ; return true ; }
 }