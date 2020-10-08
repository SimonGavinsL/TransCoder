class X { static int nextPowerOf2 ( int n ) { int count = 0 ; while ( n != 0 ) { n >>= 1 ; count += 1 ; } return 1 << count ; }
 }