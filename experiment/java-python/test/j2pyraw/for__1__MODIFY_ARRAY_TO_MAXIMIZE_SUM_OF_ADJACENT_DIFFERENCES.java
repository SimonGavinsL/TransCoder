class X { static int maximumDifferenceSum ( int arr [ ] , int N ) { int dp [ ] [ ] = new int [ N ] [ 2 ] ; return Math . max ( dp [ N - 1 ] [ 0 ] , dp [ N - 1 ] [ 1 ] ) ; }
 }