static int chordCnt ( int A ) { int n = 2 * A ; int [ ] dpArray = new int [ n + 1 ] ; dpArray [ 0 ] = 1 ; dpArray [ 2 ] = 1 ; return dpArray [ n ] ; }
