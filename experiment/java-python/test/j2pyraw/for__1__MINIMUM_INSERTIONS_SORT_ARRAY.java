class X { static int minInsertionStepToSortArray ( int arr [ ] , int N ) { int [ ] lis = new int [ N ] ; int max = 0 ; for ( int i = 0 ; i < N ; i ++ ) if ( max < lis [ i ] ) max = lis [ i ] ; return ( N - max ) ; }
 }