static int recSearch ( int arr [ ] , int l , int r , int x ) { if ( arr [ r ] == x ) return r ; return recSearch ( arr , l + 1 , r - 1 , x ) ; }
