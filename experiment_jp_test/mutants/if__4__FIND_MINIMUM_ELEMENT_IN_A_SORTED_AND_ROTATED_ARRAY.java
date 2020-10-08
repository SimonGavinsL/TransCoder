static int findMin ( int arr [ ] , int low , int high ) { int mid = low + ( high - low ) / 2 ; return findMin ( arr , mid + 1 , high ) ; }
