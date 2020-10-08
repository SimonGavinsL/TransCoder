static long exponentiation ( long base , long exp ) { long t = exponentiation ( base , exp / 2 ) ; t = ( t * t ) % N ; }
