class X { static long yMod ( long y , long x ) { if ( x > 63 ) return y ; return ( y % ( 1 << ( int ) x ) ) ; }
 }