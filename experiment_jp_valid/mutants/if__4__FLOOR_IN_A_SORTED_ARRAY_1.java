static int floorSearch ( int arr [ ] , int low , int high , int x ) { int mid = ( low + high ) / 2 ; return floorSearch ( arr , mid + 1 , high , x ) ; }
