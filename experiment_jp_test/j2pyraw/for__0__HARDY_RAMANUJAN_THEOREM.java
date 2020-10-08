class X { static int exactPrimeFactorCount ( int n ) { int count = 0 ; if ( n % 2 == 0 ) { count ++ ; while ( n % 2 == 0 ) n = n / 2 ; } if ( n > 2 ) count ++ ; return count ; }
 }