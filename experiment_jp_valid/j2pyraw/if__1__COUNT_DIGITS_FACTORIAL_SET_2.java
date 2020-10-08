class X { static long findDigits ( int n ) { double x = ( n * Math . log10 ( n / M_E ) + Math . log10 ( 2 * M_PI * n ) / 2.0 ) ; return ( long ) Math . floor ( x ) + 1 ; }
 }