static long maxPrimeFactors ( long n ) { long maxPrime = - 1 ; while ( n % 2 == 0 ) { maxPrime = 2 ; n >>= 1 ; } if ( n > 2 ) maxPrime = n ; return maxPrime ; }
