static void findAndPrintUncommonChars ( String str1 , String str2 ) { int present [ ] = new int [ MAX_CHAR ] ; int l1 = str1 . length ( ) ; int l2 = str2 . length ( ) ; for ( int i = 0 ; i < MAX_CHAR ; i ++ ) { if ( present [ i ] == 1 || present [ i ] == 2 ) { System . out . print ( ( char ) ( i + ' a ' ) + " ▁ " ) ; } } }