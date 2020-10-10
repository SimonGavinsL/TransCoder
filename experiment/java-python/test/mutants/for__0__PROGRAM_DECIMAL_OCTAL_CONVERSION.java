static void decToOctal ( int n ) { int [ ] octalNum = new int [ 100 ] ; int i = 0 ; while ( n != 0 ) { octalNum [ i ] = n % 8 ; n = n / 8 ; i ++ ; } }
