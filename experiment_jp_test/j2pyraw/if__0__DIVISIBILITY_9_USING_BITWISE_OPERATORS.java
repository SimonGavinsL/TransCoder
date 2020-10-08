class X { static boolean isDivBy9 ( int n ) { if ( n < 9 ) return false ; return isDivBy9 ( ( int ) ( n > > 3 ) - ( int ) ( n & 7 ) ) ; }
 }