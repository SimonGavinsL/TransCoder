class X { static int findGreatest ( int arr [ ] , int n ) { Map < Integer , Integer > m = new HashMap < > ( ) ; Arrays . sort ( arr ) ; for ( int i = n - 1 ; i > 1 ; i -- ) { for ( int j = 0 ; j < i && arr [ j ] <= Math . sqrt ( arr [ i ] ) ; j ++ ) { if ( arr [ i ] % arr [ j ] == 0 ) { int result = arr [ i ] / arr [ j ] ; if ( result != arr [ j ] && m . get ( result ) == null || m . get ( result ) > 0 ) { return arr [ i ] ; } else if ( result == arr [ j ] && m . get ( result ) > 1 ) { return arr [ i ] ; } } } } return - 1 ; }
 }