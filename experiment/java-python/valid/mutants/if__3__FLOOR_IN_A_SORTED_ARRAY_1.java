static int floorSearch ( int arr [ ] , int low , int high , int x ) { int mid = ( low + high ) / 2 ; if ( x < arr [ mid ] ) return floorSearch ( arr , low , mid - 1 , x ) ; return floorSearch ( arr , mid + 1 , high , x ) ; }