class X { public static void printPairs ( int arr [ ] , int n ) { Vector < Integer > v = new Vector < Integer > ( ) ; if ( v . size ( ) == 0 ) return ; Collections . sort ( v ) ; for ( int i = 0 ; i < v . size ( ) ; i ++ ) System . out . print ( - v . get ( i ) + " ▁ " + v . get ( i ) ) ; }
 }