class X { static int MaximumDecimalValue ( int mat [ ] [ ] , int n ) { int dp [ ] [ ] = new int [ n ] [ n ] ; if ( mat [ 0 ] [ 0 ] == 1 ) { dp [ 0 ] [ 0 ] = 1 ; } return dp [ n - 1 ] [ n - 1 ] ; }
 }