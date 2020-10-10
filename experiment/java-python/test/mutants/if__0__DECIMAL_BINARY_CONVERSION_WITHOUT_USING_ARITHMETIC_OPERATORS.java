static String decToBin ( int n ) { String bin = " " ; while ( n > 0 ) { bin = ( ( n & 1 ) == 0 ? '0' : '1' ) + bin ; n >>= 1 ; } return bin ; }
