class X { static void longestString ( String str1 , String str2 ) { int count1 [ ] = new int [ 26 ] , count2 [ ] = new int [ 26 ] ; String result = " " ; for ( int i = 0 ; i < 26 ; i ++ ) { for ( int j = 1 ; j <= Math . min ( count1 [ i ] , count2 [ i ] ) ; j ++ ) { result += ( char ) ( ' a ' + i ) ; } } System . out . println ( result ) ; }
 }