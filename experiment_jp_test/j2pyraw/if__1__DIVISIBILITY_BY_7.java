class X { static boolean isDivisibleBy7 ( int num ) { if ( num < 10 ) return false ; return isDivisibleBy7 ( num / 10 - 2 * ( num - num / 10 * 10 ) ) ; }
 }