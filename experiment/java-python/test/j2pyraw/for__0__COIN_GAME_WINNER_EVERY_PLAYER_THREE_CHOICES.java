class X { static boolean findWinner ( int x , int y , int n ) { boolean [ ] dp = new boolean [ n + 1 ] ; Arrays . fill ( dp , false ) ; dp [ 0 ] = false ; dp [ 1 ] = true ; return dp [ n ] ; }
 }