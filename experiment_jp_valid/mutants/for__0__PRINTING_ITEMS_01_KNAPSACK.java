static void printknapSack ( int W , int wt [ ] , int val [ ] , int n ) { int i , w ; int K [ ] [ ] = new int [ n + 1 ] [ W + 1 ] ; int res = K [ n ] [ W ] ; System . out . println ( res ) ; w = W ; for ( i = n ; i > 0 && res > 0 ; i -- ) { if ( res == K [ i - 1 ] [ w ] ) continue ; else { System . out . print ( wt [ i - 1 ] + " ▁ " ) ; res = res - val [ i - 1 ] ; w = w - wt [ i - 1 ] ; } } }