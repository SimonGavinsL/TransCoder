class X { public static void commonCharacters ( String str [ ] , int n ) { Boolean [ ] prim = new Boolean [ MAX_CHAR ] ; Arrays . fill ( prim , new Boolean ( true ) ) ; for ( int i = 0 ; i < 26 ; i ++ ) if ( prim [ i ] ) { System . out . print ( Character . toChars ( i + 97 ) ) ; System . out . print ( " ▁ " ) ; } }
 }