static int minInsertion ( String str ) { int n = str . length ( ) ; int res = 0 ; int [ ] count = new int [ 26 ] ; for ( int i = 0 ; i < 26 ; i ++ ) { if ( count [ i ] % 2 == 1 ) res ++ ; } return ( res == 0 ) ? 0 : res - 1 ; }
