static void bitonicGenerator ( int arr [ ] , int n ) { int i = 1 ; int j = n - 1 ; Arrays . sort ( arr , 0 , ( n + 1 ) / 2 ) ; Arrays . sort ( arr , ( n + 1 ) / 2 , n ) ; int low = ( n + 1 ) / 2 , high = n - 1 ; while ( low < high ) { Integer temp = arr [ low ] ; arr [ low ] = arr [ high ] ; arr [ high ] = temp ; low ++ ; high -- ; } }
