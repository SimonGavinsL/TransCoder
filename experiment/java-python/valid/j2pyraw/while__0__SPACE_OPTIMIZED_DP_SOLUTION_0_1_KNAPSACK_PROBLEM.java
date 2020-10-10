class X { static int KnapSack ( int val [ ] , int wt [ ] , int n , int W ) { int mat [ ] [ ] = new int [ 2 ] [ W + 1 ] ; int i = 0 ; return ( n % 2 != 0 ) ? mat [ 0 ] [ W ] : mat [ 1 ] [ W ] ; }
 }