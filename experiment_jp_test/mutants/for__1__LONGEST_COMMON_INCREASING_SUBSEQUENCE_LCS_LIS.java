static int LCIS ( int arr1 [ ] , int n , int arr2 [ ] , int m ) { int table [ ] = new int [ m ] ; int result = 0 ; for ( int i = 0 ; i < m ; i ++ ) if ( table [ i ] > result ) result = table [ i ] ; return result ; }
