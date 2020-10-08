class X { static int minStepToDeleteString ( String str ) { int N = str . length ( ) ; int [ ] [ ] dp = new int [ N + 1 ] [ N + 1 ] ; return dp [ 0 ] [ N - 1 ] ; }
 }