static long exponentiation ( long base , long exp ) { long t = exponentiation ( base , exp / 2 ) ; t = ( t * t ) % N ; if ( exp % 2 == 0 ) return t ; else return ( ( base % N ) * t ) % N ; }
