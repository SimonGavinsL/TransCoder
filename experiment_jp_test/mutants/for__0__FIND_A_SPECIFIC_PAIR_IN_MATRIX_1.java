static int findMaxValue ( int N , int mat [ ] [ ] ) { int maxValue = Integer . MIN_VALUE ; int maxArr [ ] [ ] = new int [ N ] [ N ] ; maxArr [ N - 1 ] [ N - 1 ] = mat [ N - 1 ] [ N - 1 ] ; int maxv = mat [ N - 1 ] [ N - 1 ] ; maxv = mat [ N - 1 ] [ N - 1 ] ; for ( int i = N - 2 ; i >= 0 ; i -- ) { if ( mat [ i ] [ N - 1 ] > maxv ) maxv = mat [ i ] [ N - 1 ] ; maxArr [ i ] [ N - 1 ] = maxv ; } for ( int i = N - 2 ; i >= 0 ; i -- ) { for ( int j = N - 2 ; j >= 0 ; j -- ) { if ( maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] > maxValue ) maxValue = maxArr [ i + 1 ] [ j + 1 ] - mat [ i ] [ j ] ; maxArr [ i ] [ j ] = Math . max ( mat [ i ] [ j ] , Math . max ( maxArr [ i ] [ j + 1 ] , maxArr [ i + 1 ] [ j ] ) ) ; } } return maxValue ; }