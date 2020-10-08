class X { public static long findWays ( int f , int d , int s ) { long mem [ ] [ ] = new long [ d + 1 ] [ s + 1 ] ; mem [ 0 ] [ 0 ] = 1 ; return mem [ d ] [ s ] ; }
 }