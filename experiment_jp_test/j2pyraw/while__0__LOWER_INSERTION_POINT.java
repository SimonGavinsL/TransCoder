class X { static int LowerInsertionPoint ( int arr [ ] , int n , int X ) { int lowerPnt = 0 ; int i = 1 ; while ( lowerPnt < n && arr [ lowerPnt ] < X ) lowerPnt ++ ; return lowerPnt ; }
 }