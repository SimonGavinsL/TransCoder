static boolean isPath ( int arr [ ] [ ] ) { arr [ 0 ] [ 0 ] = 1 ; for ( int i = 1 ; i < 5 ; i ++ ) for ( int j = 1 ; j < 5 ; j ++ ) if ( arr [ i ] [ j ] != - 1 ) arr [ i ] [ j ] = Math . max ( arr [ i ] [ j - 1 ] , arr [ i - 1 ] [ j ] ) ; return ( arr [ 5 - 1 ] [ 5 - 1 ] == 1 ) ; }