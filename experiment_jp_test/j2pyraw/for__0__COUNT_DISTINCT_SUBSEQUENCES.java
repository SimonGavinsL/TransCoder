class X { static int countSub ( String str ) { int [ ] last = new int [ MAX_CHAR ] ; Arrays . fill ( last , - 1 ) ; int n = str . length ( ) ; int [ ] dp = new int [ n + 1 ] ; dp [ 0 ] = 1 ; return dp [ n ] ; }
 }