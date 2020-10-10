static int countDigits ( int a , int b ) { int count = 0 ; int p = Math . abs ( a * b ) ; while ( p > 0 ) { count ++ ; p = p / 10 ; } return count ; }
