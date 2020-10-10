private static int minCost ( int cost [ ] [ ] , int m , int n ) { int i , j ; int tc [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ; tc [ 0 ] [ 0 ] = cost [ 0 ] [ 0 ] ; return tc [ m ] [ n ] ; }
