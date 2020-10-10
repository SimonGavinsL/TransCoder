class X { static long countStrs ( int n ) { long [ ] [ ] dp = new long [ n + 1 ] [ 27 ] ; long sum = 0 ; for ( int i = 0 ; i <= 25 ; i ++ ) { sum = ( sum + dp [ n ] [ i ] ) ; } return sum ; }
 }