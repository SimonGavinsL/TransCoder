class X { static void printDistinct ( String str ) { int n = str . length ( ) ; int [ ] count = new int [ MAX_CHAR ] ; int [ ] index = new int [ MAX_CHAR ] ; Arrays . sort ( index ) ; for ( int i = 0 ; i < MAX_CHAR && index [ i ] != n ; i ++ ) System . out . print ( str . charAt ( index [ i ] ) ) ; }
 }