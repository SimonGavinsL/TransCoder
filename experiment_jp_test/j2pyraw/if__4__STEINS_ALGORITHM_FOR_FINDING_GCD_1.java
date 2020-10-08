class X { static int gcd ( int a , int b ) { if ( a > b ) return gcd ( ( a - b ) > > 1 , b ) ; return gcd ( ( b - a ) > > 1 , a ) ; }
 }