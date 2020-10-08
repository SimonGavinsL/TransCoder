class X { static int countSol ( int coeff [ ] , int n , int rhs ) { int dp [ ] = new int [ rhs + 1 ] ; Arrays . fill ( dp , 0 ) ; dp [ 0 ] = 1 ; return dp [ rhs ] ; }
 }