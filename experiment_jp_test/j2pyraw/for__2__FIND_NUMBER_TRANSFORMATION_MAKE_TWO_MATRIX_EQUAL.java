class X { static int countOps ( int A [ ] [ ] , int B [ ] [ ] , int m , int n ) { int result = 0 ; for ( int j = 0 ; j < m ; j ++ ) result += Math . abs ( A [ 0 ] [ j ] - A [ 0 ] [ 0 ] ) ; return ( result ) ; }
 }