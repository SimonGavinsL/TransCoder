static int SieveOfAtkin ( int limit ) { if ( limit > 2 ) System . out . print ( 2 + " ▁ " ) ; if ( limit > 3 ) System . out . print ( 3 + " ▁ " ) ; boolean sieve [ ] = new boolean [ limit ] ; for ( int a = 5 ; a < limit ; a ++ ) if ( sieve [ a ] ) System . out . print ( a + " ▁ " ) ; return 0 ; }
