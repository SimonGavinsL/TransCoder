static void printMat ( int degseq [ ] , int n ) { int [ ] [ ] mat = new int [ n ] [ n ] ; System . out . print ( " \n " + setw ( 3 ) + " ▁ ▁ ▁ ▁ ▁ " ) ; System . out . print ( " \n \n " ) ; for ( int i = 0 ; i < n ; i ++ ) { System . out . print ( setw ( 4 ) + " ( " + i + " ) " ) ; for ( int j = 0 ; j < n ; j ++ ) System . out . print ( setw ( 5 ) + mat [ i ] [ j ] ) ; System . out . print ( " \n " ) ; } }
