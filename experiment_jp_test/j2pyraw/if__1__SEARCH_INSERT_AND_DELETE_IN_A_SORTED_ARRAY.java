class X { static int binarySearch ( int arr [ ] , int low , int high , int key ) { int mid = ( low + high ) / 2 ; if ( key > arr [ mid ] ) return binarySearch ( arr , ( mid + 1 ) , high , key ) ; return binarySearch ( arr , low , ( mid - 1 ) , key ) ; }
 }