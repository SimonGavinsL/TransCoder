class X { static void constructTree ( int n , int d , int h ) { if ( d > 2 * h ) { System . out . println ( " - 1" ) ; return ; } if ( d > h ) { System . out . println ( "1" + " ▁ " + ( h + 2 ) ) ; for ( int i = h + 2 ; i <= d ; i ++ ) { System . out . println ( i + " ▁ " + ( i + 1 ) ) ; } } }
 }