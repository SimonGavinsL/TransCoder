class X { public static int minMaxProduct ( int arr1 [ ] , int arr2 [ ] , int n1 , int n2 ) { int max = arr1 [ 0 ] ; int min = arr2 [ 0 ] ; int i ; while ( i < n2 ) { if ( arr2 [ i ] < min ) min = arr2 [ i ] ; i ++ ; } return max * min ; }
 }