public static String recursiveReverse ( char [ ] str ) { Stack < Character > st = new Stack < > ( ) ; for ( int i = 0 ; i < str . length ; i ++ ) { str [ i ] = st . peek ( ) ; st . pop ( ) ; } return String . valueOf ( str ) ; }
