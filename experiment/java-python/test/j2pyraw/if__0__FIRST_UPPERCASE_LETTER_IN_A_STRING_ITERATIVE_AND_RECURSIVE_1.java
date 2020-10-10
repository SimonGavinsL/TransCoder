class X { static char first ( String str , int i ) { if ( Character . isUpperCase ( str . charAt ( i ) ) ) return str . charAt ( i ) ; return first ( str , i + 1 ) ; }
 }