static void kSmallestPair ( int arr1 [ ] , int n1 , int arr2 [ ] , int n2 , int k ) { int index2 [ ] = new int [ n1 ] ; while ( k > 0 ) { int min_sum = Integer . MAX_VALUE ; int min_index = 0 ; for ( int i1 = 0 ; i1 < n1 ; i1 ++ ) { if ( index2 [ i1 ] < n2 && arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] < min_sum ) { min_index = i1 ; min_sum = arr1 [ i1 ] + arr2 [ index2 [ i1 ] ] ; } } System . out . print ( " ( " + arr1 [ min_index ] + " , ▁ " + arr2 [ index2 [ min_index ] ] + " ) ▁ " ) ; index2 [ min_index ] ++ ; k -- ; } }
