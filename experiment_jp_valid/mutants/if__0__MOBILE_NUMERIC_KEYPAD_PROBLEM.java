static int getCount ( char keypad [ ] [ ] , int n ) { if ( n == 1 ) return 10 ; int [ ] odd = new int [ 10 ] ; int [ ] even = new int [ 10 ] ; int i = 0 , j = 0 , useOdd = 0 , totalCount = 0 ; totalCount = 0 ; if ( useOdd == 1 ) { for ( i = 0 ; i <= 9 ; i ++ ) totalCount += even [ i ] ; } else { for ( i = 0 ; i <= 9 ; i ++ ) totalCount += odd [ i ] ; } return totalCount ; }