class X { static int binarySearch ( int arr [ ] , int low , int high , int key ) { int mid = ( low + high ) / 2 ; return binarySearch ( arr , low , ( mid - 1 ) , key ) ; }
 }