class X { static int countDer ( int n ) { if ( n == 2 ) return 1 ; return ( n - 1 ) * ( countDer ( n - 1 ) + countDer ( n - 2 ) ) ; }
 }