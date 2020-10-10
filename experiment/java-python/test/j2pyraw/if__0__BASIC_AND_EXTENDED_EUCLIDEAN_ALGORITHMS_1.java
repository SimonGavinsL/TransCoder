class X { public static int gcdExtended ( int a , int b , int x , int y ) { int x1 = 1 , y1 = 1 ; int gcd = gcdExtended ( b % a , a , x1 , y1 ) ; x = y1 - ( b / a ) * x1 ; y = x1 ; return gcd ; }
 }