class X { static int fib ( int n , int a , int b ) { if ( n == 1 ) return b ; return fib ( n - 1 , b , a + b ) ; }
 }