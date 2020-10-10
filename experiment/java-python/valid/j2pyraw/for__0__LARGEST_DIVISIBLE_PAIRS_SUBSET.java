class X { static int largestSubset ( int [ ] a , int n ) { Arrays . sort ( a ) ; int [ ] dp = new int [ n ] ; dp [ n - 1 ] = 1 ; return Arrays . stream ( dp ) . max ( ) . getAsInt ( ) ; }
 }