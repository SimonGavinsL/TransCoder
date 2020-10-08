static int maxSumIS ( int arr [ ] , int n ) { int i , j , max = 0 ; int msis [ ] = new int [ n ] ; for ( i = 0 ; i < n ; i ++ ) if ( max < msis [ i ] ) max = msis [ i ] ; return max ; }
