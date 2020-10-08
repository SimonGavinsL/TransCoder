class X { static int sumofoddFactors ( int n ) { int res = 1 ; while ( n % 2 == 0 ) n = n / 2 ; if ( n >= 2 ) res *= ( 1 + n ) ; return res ; }
 }