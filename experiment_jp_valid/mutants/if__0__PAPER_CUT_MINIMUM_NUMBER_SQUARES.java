static int minimumSquare ( int a , int b ) { int result = 0 , rem = 0 ; while ( b > 0 ) { result += a / b ; rem = a % b ; a = b ; b = rem ; } return result ; }
