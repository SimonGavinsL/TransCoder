static void pushZerosToEnd ( int arr [ ] , int n ) { int count = 0 ; for ( int i = 0 ; i < n ; i ++ ) if ( arr [ i ] != 0 ) arr [ count ++ ] = arr [ i ] ; while ( count < n ) arr [ count ++ ] = 0 ; }
