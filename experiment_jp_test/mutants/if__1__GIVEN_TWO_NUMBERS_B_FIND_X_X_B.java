static void modularEquation ( int a , int b ) { int count = 0 ; int n = a - b ; int y = ( int ) Math . sqrt ( a - b ) ; if ( y * y == n && y > b ) count -- ; System . out . println ( count ) ; }
