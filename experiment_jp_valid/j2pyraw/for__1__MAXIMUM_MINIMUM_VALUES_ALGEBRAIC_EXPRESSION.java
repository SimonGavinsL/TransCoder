class X { static void minMaxValues ( int [ ] arr , int n , int m ) { int sum = 0 ; boolean dp [ ] [ ] = new boolean [ MAX + 1 ] [ MAX * MAX + 1 ] ; dp [ 0 ] [ 0 ] = true ; double max_value = - 1 * INF , min_value = INF ; for ( int i = 0 ; i < MAX * MAX + 1 ; i ++ ) { if ( dp [ n ] [ i ] ) { int temp = i - 50 * n ; max_value = Math . max ( max_value , temp * ( sum - temp ) ) ; min_value = Math . min ( min_value , temp * ( sum - temp ) ) ; } } System . out . print ( " Maximum ▁ Value : ▁ " + ( int ) max_value + " \n " + " Minimum ▁ Value : ▁ " + ( int ) min_value + " \n " ) ; }
 }