class X { static int getPairsCount ( int n , int sum ) { HashMap < Integer , Integer > hm = new HashMap < > ( ) ; int twice_count = 0 ; for ( int i = 0 ; i < n ; i ++ ) { if ( hm . get ( sum - arr [ i ] ) != null ) twice_count += hm . get ( sum - arr [ i ] ) ; if ( sum - arr [ i ] == arr [ i ] ) twice_count -- ; } return twice_count / 2 ; }
 }