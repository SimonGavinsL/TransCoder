public static int maxLenSub ( int arr [ ] , int n ) { int mls [ ] = new int [ n ] , max = 0 ; for ( int i = 0 ; i < n ; i ++ ) if ( max < mls [ i ] ) max = mls [ i ] ; return max ; }
