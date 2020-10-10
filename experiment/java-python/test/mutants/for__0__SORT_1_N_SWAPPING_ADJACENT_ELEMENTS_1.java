static int sortedAfterSwap ( int [ ] A , int [ ] B , int n ) { int t = 0 ; for ( int i = 0 ; i < n ; i ++ ) { if ( A [ i ] != i + 1 ) return 0 ; } return 1 ; }
