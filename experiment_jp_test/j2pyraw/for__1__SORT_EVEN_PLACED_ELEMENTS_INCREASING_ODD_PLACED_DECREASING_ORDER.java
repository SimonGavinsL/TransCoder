class X { static void bitonicGenerator ( int arr [ ] , int n ) { Vector < Integer > evenArr = new Vector < Integer > ( ) ; Vector < Integer > oddArr = new Vector < Integer > ( ) ; Collections . sort ( evenArr ) ; Collections . sort ( oddArr , Collections . reverseOrder ( ) ) ; int i = 0 ; for ( int j = 0 ; j < oddArr . size ( ) ; j ++ ) { arr [ i ++ ] = oddArr . get ( j ) ; } }
 }