int maxLen ( int arr [ ] , int n ) { HashMap < Integer , Integer > hM = new HashMap < Integer , Integer > ( ) ; int sum = 0 ; int max_len = 0 ; int ending_index = - 1 ; int start_index = 0 ; for ( int i = 0 ; i < n ; i ++ ) { arr [ i ] = ( arr [ i ] == - 1 ) ? 0 : 1 ; } int end = ending_index - max_len + 1 ; System . out . println ( end + " ▁ to ▁ " + ending_index ) ; return max_len ; }