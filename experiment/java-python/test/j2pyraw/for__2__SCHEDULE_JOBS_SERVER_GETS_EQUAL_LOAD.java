class X { static int solve ( int a [ ] , int b [ ] , int n ) { int i ; int s = 0 ; if ( n == 1 ) return a [ 0 ] + b [ 0 ] ; if ( s % n != 0 ) return - 1 ; int x = s / n ; return x ; }
 }