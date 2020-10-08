static int countWays ( int n ) { int [ ] A = new int [ n + 1 ] ; int [ ] B = new int [ n + 1 ] ; A [ 0 ] = 1 ; A [ 1 ] = 0 ; B [ 0 ] = 0 ; B [ 1 ] = 1 ; return A [ n ] ; }
