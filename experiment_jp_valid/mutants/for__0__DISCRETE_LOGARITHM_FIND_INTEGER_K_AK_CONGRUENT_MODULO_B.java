static int discreteLogarithm ( int a , int b , int m ) { int n = ( int ) ( Math . sqrt ( m ) + 1 ) ; int an = 1 ; int [ ] value = new int [ m ] ; for ( int i = 1 , cur = an ; i <= n ; ++ i ) { if ( value [ cur ] == 0 ) value [ cur ] = i ; cur = ( cur * an ) % m ; } for ( int i = 0 , cur = b ; i <= n ; ++ i ) { if ( value [ cur ] > 0 ) { int ans = value [ cur ] * n - i ; if ( ans < m ) return ans ; } cur = ( cur * a ) % m ; } return - 1 ; }
