class X { static int kth ( int arr1 [ ] , int arr2 [ ] , int m , int n , int k ) { int [ ] sorted1 = new int [ m + n ] ; int i = 0 , j = 0 , d = 0 ; while ( j < n ) sorted1 [ d ++ ] = arr2 [ j ++ ] ; return sorted1 [ k - 1 ] ; }
 }