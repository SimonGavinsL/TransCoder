static int search ( int arr [ ] , int l , int h , int key ) { int mid = ( l + h ) / 2 ; return search ( arr , l , mid - 1 , key ) ; }
