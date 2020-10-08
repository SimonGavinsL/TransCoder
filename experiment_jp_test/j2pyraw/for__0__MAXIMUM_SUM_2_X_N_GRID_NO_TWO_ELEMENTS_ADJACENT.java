class X { public static int maxSum ( int grid [ ] [ ] , int n ) { int incl = Math . max ( grid [ 0 ] [ 0 ] , grid [ 1 ] [ 0 ] ) ; int excl = 0 , excl_new ; return Math . max ( excl , incl ) ; }
 }