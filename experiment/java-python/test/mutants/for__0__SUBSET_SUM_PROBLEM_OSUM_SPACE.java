static boolean isSubsetSum ( int arr [ ] , int n , int sum ) { boolean subset [ ] [ ] = new boolean [ 2 ] [ sum + 1 ] ; return subset [ n % 2 ] [ sum ] ; }
