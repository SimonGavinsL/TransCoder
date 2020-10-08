public static void rearrange ( int arr [ ] , int n ) { int max_idx = n - 1 , min_idx = 0 ; int max_elem = arr [ n - 1 ] + 1 ; for ( int i = 0 ; i < n ; i ++ ) arr [ i ] = arr [ i ] / max_elem ; }
