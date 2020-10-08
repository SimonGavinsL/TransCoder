class X { static int countWays ( int N ) { if ( N == 1 ) return 4 ; int countB = 1 , countS = 1 , prev_countB , prev_countS ; int result = countS + countB ; return ( result * result ) ; }
 }