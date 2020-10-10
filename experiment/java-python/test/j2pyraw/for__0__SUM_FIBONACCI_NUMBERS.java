class X { static int calculateSum ( int n ) { if ( n <= 0 ) return 0 ; int fibo [ ] = new int [ n + 1 ] ; fibo [ 0 ] = 0 ; fibo [ 1 ] = 1 ; int sum = fibo [ 0 ] + fibo [ 1 ] ; return sum ; }
 }