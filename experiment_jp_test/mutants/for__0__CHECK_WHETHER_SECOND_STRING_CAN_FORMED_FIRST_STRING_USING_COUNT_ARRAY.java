static boolean canMakeStr2 ( String str1 , String str2 ) { int [ ] count = new int [ MAX ] ; char [ ] str3 = str1 . toCharArray ( ) ; char [ ] str4 = str2 . toCharArray ( ) ; for ( int i = 0 ; i < str4 . length ; i ++ ) { if ( count [ str4 [ i ] ] == 0 ) return false ; count [ str4 [ i ] ] -- ; } return true ; }
