static void deleteElements ( int arr [ ] , int n , int k ) { Stack < Integer > s = new Stack < > ( ) ; s . push ( arr [ 0 ] ) ; int count = 0 ; int m = s . size ( ) ; Integer [ ] v = new Integer [ m ] ; while ( ! s . empty ( ) ) { v [ -- m ] = s . peek ( ) ; s . pop ( ) ; } ; System . out . println ( " " ) ; }
