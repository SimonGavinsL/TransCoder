static int FindMaxProduct ( int arr [ ] [ ] , int n ) { int max = 0 , result ; for ( int i = 0 ; i < n ; i ++ ) { for ( int j = 0 ; j < n ; j ++ ) { if ( ( j - 3 ) >= 0 ) { result = arr [ i ] [ j ] * arr [ i ] [ j - 1 ] * arr [ i ] [ j - 2 ] * arr [ i ] [ j - 3 ] ; if ( max < result ) max = result ; } if ( ( i - 3 ) >= 0 ) { result = arr [ i ] [ j ] * arr [ i - 1 ] [ j ] * arr [ i - 2 ] [ j ] * arr [ i - 3 ] [ j ] ; if ( max < result ) max = result ; } if ( ( i - 3 ) >= 0 && ( j - 3 ) >= 0 ) { result = arr [ i ] [ j ] * arr [ i - 1 ] [ j - 1 ] * arr [ i - 2 ] [ j - 2 ] * arr [ i - 3 ] [ j - 3 ] ; if ( max < result ) max = result ; } } } return max ; }
