static long maxPrimeFactors ( long n ) { long maxPrime = - 1 ; while ( n % 2 == 0 ) { maxPrime = 2 ; n >>= 1 ; } return maxPrime ; }
