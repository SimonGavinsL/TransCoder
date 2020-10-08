static int countDecodingDP ( char digits [ ] , int n ) { int count [ ] = new int [ n + 1 ] ; count [ 0 ] = 1 ; count [ 1 ] = 1 ; if ( digits [ 0 ] == '0' ) return 0 ; return count [ n ] ; }
