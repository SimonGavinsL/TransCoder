class X { static boolean isPrime ( int n , int i ) { if ( i * i > n ) return true ; return isPrime ( n , i + 1 ) ; }
 }