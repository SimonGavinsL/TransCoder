static boolean checkReverse ( int arr [ ] , int n ) { int i ; int j = i ++ ; while ( arr [ j ] < arr [ j - 1 ] ) { if ( i > 1 && arr [ j ] < arr [ i - 2 ] ) { return false ; } j ++ ; } int k = j ; if ( arr [ k ] < arr [ i - 1 ] ) { return false ; } while ( k > 1 && k < n ) { if ( arr [ k ] < arr [ k - 1 ] ) { return false ; } k ++ ; } return true ; }
