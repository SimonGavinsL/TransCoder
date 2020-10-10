static int countFact ( int low , int high ) { int fact = 1 , x = 1 ; int res = 0 ; while ( fact <= high ) { res ++ ; fact = fact * x ; x ++ ; } return res ; }
