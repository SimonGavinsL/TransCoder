static int maxLength ( String s , int n ) { int dp [ ] [ ] = new int [ n ] [ n ] ; for ( int l = 2 ; l < n ; l ++ ) { for ( int i = 0 , j = l ; j < n ; i ++ , j ++ ) { if ( s . charAt ( i ) == ' ( ' && s . charAt ( j ) == ' ) ' ) dp [ i ] [ j ] = 2 + dp [ i + 1 ] [ j - 1 ] ; for ( int k = i ; k < j ; k ++ ) dp [ i ] [ j ] = Math . max ( dp [ i ] [ j ] , dp [ i ] [ k ] + dp [ k + 1 ] [ j ] ) ; } } return dp [ 0 ] [ n - 1 ] ; }
