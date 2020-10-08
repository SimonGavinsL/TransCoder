static int lis ( int arr [ ] , int n ) { int lis [ ] = new int [ n ] ; int i , j , max = 0 ; for ( i = 0 ; i < n ; i ++ ) if ( max < lis [ i ] ) max = lis [ i ] ; return max ; }
