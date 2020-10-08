class X { static int arraySortedOrNot ( int arr [ ] , int n ) { if ( arr [ n - 1 ] < arr [ n - 2 ] ) return 0 ; return arraySortedOrNot ( arr , n - 1 ) ; }
 }