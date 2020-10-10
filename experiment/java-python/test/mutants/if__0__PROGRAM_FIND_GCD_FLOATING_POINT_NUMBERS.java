static double gcd ( double a , double b ) { if ( Math . abs ( b ) < 0.001 ) return a ; else return ( gcd ( b , a - Math . floor ( a / b ) * b ) ) ; }
