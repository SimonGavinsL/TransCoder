static void printkthnode ( Vector < pair > adj [ ] , int wt [ ] , int n , int k ) { for ( int i = 0 ; i < n ; i ++ ) { if ( adj [ i ] . size ( ) >= k ) System . out . print ( adj [ i ] . get ( adj [ i ] . size ( ) - k ) . second + " ▁ " ) ; else System . out . print ( " - 1" ) ; } }
