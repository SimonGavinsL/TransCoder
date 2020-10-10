class X { static int findRepeatingElement ( int arr [ ] , int low , int high ) { int mid = ( low + high ) / 2 ; return findRepeatingElement ( arr , mid + 1 , high ) ; }
 }