static boolean checkReverse ( int arr [ ] , int n ) { int i ; int j = i ++ ; int k = j ; while ( k > 1 && k < n ) { if ( arr [ k ] < arr [ k - 1 ] ) { return false ; } k ++ ; } return true ; }
