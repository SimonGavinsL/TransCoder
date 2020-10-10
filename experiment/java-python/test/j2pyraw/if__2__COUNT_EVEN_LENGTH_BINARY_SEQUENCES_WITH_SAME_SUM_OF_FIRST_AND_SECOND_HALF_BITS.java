class X { static int countSeq ( int n , int diff ) { int res = countSeq ( n - 1 , diff + 1 ) + 2 * countSeq ( n - 1 , diff ) + countSeq ( n - 1 , diff - 1 ) ; return res ; }
 }