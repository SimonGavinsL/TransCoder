static int costToBalance ( String s ) { if ( s . length ( ) == 0 ) System . out . println ( 0 ) ; int ans = 0 ; int o = 0 , c = 0 ; if ( o != c ) return - 1 ; int [ ] a = new int [ s . length ( ) ] ; if ( s . charAt ( 0 ) == ' ( ' ) a [ 0 ] = 1 ; else a [ 0 ] = - 1 ; if ( a [ 0 ] < 0 ) ans += Math . abs ( a [ 0 ] ) ; return ans ; }
