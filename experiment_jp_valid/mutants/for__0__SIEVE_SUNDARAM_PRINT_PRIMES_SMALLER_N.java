static int SieveOfSundaram ( int n ) { int nNew = ( n - 2 ) / 2 ; boolean marked [ ] = new boolean [ nNew + 1 ] ; Arrays . fill ( marked , false ) ; if ( n > 2 ) System . out . print ( 2 + " ▁ " ) ; for ( int i = 1 ; i <= nNew ; i ++ ) if ( marked [ i ] == false ) System . out . print ( 2 * i + 1 + " ▁ " ) ; return - 1 ; }
