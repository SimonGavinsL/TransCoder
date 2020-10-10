class X { static boolean sortedAfterSwap ( int A [ ] , boolean B [ ] , int n ) { int i , j ; for ( i = 0 ; i < n ; i ++ ) { if ( A [ i ] != i + 1 ) { return false ; } } return true ; }
 }