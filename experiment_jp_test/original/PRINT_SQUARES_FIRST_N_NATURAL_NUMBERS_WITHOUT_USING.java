static void printSquares ( int n ) { int square = 0 , prev_x = 0 ; for ( int x = 0 ; x < n ; x ++ ) { square = ( square + x + prev_x ) ; System . out . print ( square + " ▁ " ) ; prev_x = x ; } }
