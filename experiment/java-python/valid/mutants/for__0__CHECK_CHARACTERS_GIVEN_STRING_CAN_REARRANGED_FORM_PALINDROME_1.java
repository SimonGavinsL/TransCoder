static boolean canFormPalindrome ( String str ) { List < Character > list = new ArrayList < Character > ( ) ; if ( str . length ( ) % 2 == 0 && list . isEmpty ( ) || ( str . length ( ) % 2 == 1 && list . size ( ) == 1 ) ) return true ; else return false ; }