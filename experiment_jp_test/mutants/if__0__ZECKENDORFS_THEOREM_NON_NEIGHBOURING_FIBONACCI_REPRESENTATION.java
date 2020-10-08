public static int nearestSmallerEqFib ( int n ) { int f1 = 0 , f2 = 1 , f3 = 1 ; while ( f3 <= n ) { f1 = f2 ; f2 = f3 ; f3 = f1 + f2 ; } return f2 ; }
