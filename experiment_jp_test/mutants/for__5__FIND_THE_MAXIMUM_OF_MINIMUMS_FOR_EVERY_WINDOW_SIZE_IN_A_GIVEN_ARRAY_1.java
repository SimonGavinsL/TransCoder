static void printMaxOfMin ( int n ) { Stack < Integer > s = new Stack < > ( ) ; int left [ ] = new int [ n + 1 ] ; int right [ ] = new int [ n + 1 ] ; while ( ! s . empty ( ) ) s . pop ( ) ; int ans [ ] = new int [ n + 1 ] ; for ( int i = 1 ; i <= n ; i ++ ) System . out . print ( ans [ i ] + " ▁ " ) ; }