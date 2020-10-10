class X { static int countRotations ( int arr [ ] , int low , int high ) { int mid = low + ( high - low ) / 2 ; return countRotations ( arr , mid + 1 , high ) ; }
 }