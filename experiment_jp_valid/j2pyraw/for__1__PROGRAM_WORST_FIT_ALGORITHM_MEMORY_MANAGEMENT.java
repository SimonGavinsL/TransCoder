class X { static void worstFit ( int blockSize [ ] , int m , int processSize [ ] , int n ) { int allocation [ ] = new int [ n ] ; System . out . println ( " \n Process ▁ No . \tProcess ▁ Size\tBlock ▁ no . " ) ; for ( int i = 0 ; i < n ; i ++ ) { System . out . print ( " ▁ ▁ ▁ " + ( i + 1 ) + " \t\t " + processSize [ i ] + " \t\t " ) ; if ( allocation [ i ] != - 1 ) System . out . print ( allocation [ i ] + 1 ) ; else System . out . print ( " Not ▁ Allocated " ) ; System . out . println ( ) ; } }
 }