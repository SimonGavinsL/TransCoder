static void rearrange ( int arr [ ] , int n ) { int i = - 1 , temp = 0 ; int pos = i + 1 , neg = 0 ; while ( pos < n && neg < pos && arr [ neg ] < 0 ) { temp = arr [ neg ] ; arr [ neg ] = arr [ pos ] ; arr [ pos ] = temp ; pos ++ ; neg += 2 ; } }
