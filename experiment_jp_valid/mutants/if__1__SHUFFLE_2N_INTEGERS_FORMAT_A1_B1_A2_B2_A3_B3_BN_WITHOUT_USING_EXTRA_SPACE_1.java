static void shufleArray ( int a [ ] , int f , int l ) { int mid = ( f + l ) / 2 ; int temp = mid + 1 ; int mmid = ( f + mid ) / 2 ; shufleArray ( a , f , mid ) ; shufleArray ( a , mid + 1 , l ) ; }
