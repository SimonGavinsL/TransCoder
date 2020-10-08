class X { static int getRemainder ( int num , int divisor ) { int i = 1 ; int product = 0 ; while ( product <= num ) { product = divisor * i ; i ++ ; } return num - ( product - divisor ) ; }
 }