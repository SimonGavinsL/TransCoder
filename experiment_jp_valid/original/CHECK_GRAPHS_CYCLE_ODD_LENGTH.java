public static boolean containsOdd ( int G [ ] [ ] , int src ) { int colorArr [ ] = new int [ V ] ; for ( int i = 0 ; i < V ; ++ i ) colorArr [ i ] = - 1 ; colorArr [ src ] = 1 ; LinkedList < Integer > q = new LinkedList < Integer > ( ) ; q . add ( src ) ; while ( ! q . isEmpty ( ) ) { int u = q . peek ( ) ; q . pop ( ) ; if ( G [ u ] [ u ] == 1 ) return true ; for ( int v = 0 ; v < V ; ++ v ) { if ( G [ u ] [ v ] == 1 && colorArr [ v ] == - 1 ) { colorArr [ v ] = 1 - colorArr [ u ] ; q . push ( v ) ; } else if ( G [ u ] [ v ] == 1 && colorArr [ v ] == colorArr [ u ] ) return true ; } } return false ; }