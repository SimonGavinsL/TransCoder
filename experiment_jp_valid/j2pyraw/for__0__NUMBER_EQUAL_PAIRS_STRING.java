class X { static int countPairs ( String s ) { int cnt [ ] = new int [ MAX ] ; int ans = 0 ; for ( int i = 0 ; i < MAX ; i ++ ) ans += cnt [ i ] * cnt [ i ] ; return ans ; }
 }