static int remAnagram ( String str1 , String str2 ) { int count1 [ ] = new int [ 26 ] ; int count2 [ ] = new int [ 26 ] ; int result = 0 ; for ( int i = 0 ; i < 26 ; i ++ ) result += Math . abs ( count1 [ i ] - count2 [ i ] ) ; return result ; }
