static int modInverse ( int a , int m ) { int m0 = m ; int y = 0 , x = 1 ; while ( a > 1 ) { int q = a / m ; int t = m ; m = a % m ; a = t ; t = y ; y = x - q * y ; x = t ; } return x ; }
