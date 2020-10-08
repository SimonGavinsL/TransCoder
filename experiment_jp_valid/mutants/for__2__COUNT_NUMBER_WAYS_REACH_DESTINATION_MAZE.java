static int countPaths ( int maze [ ] [ ] ) { if ( maze [ 0 ] [ 0 ] == - 1 ) return 0 ; return ( maze [ R - 1 ] [ C - 1 ] > 0 ) ? maze [ R - 1 ] [ C - 1 ] : 0 ; }
