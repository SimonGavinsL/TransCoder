static int minRemovalsDP ( int arr [ ] , int n ) { int longest_start = - 1 , longest_end = 0 ; if ( longest_start == - 1 ) { return n ; } return ( n - ( longest_end - longest_start + 1 ) ) ; }
