class X { static void findString ( String str , int n , int k ) { String str2 = str ; int p = 0 ; if ( p < k ) { for ( int i = n - 1 ; i >= 0 ; i -- ) if ( str . charAt ( i ) == ' a ' ) { str2 = str2 . substring ( 0 , i ) + ' b ' + str2 . substring ( i + 1 ) ; p ++ ; if ( p == k ) break ; } } System . out . println ( str2 ) ; }
 }