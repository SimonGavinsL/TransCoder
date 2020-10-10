static int gcd ( int a , int b ) { if ( ( ~ b & 1 ) == 1 ) return gcd ( a , b > > 1 ) ; if ( a > b ) return gcd ( ( a - b ) > > 1 , b ) ; return gcd ( ( b - a ) > > 1 , a ) ; }
