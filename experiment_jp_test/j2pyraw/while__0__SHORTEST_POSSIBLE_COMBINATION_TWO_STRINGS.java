class X { static void printSuperSeq ( String a , String b ) { int m = a . length ( ) , n = b . length ( ) ; int [ ] [ ] dp = new int [ m + 1 ] [ n + 1 ] ; String res = " " ; int i = m , j = n ; while ( i > 0 ) { res = a . charAt ( i - 1 ) + res ; i -- ; } while ( j > 0 ) { res = b . charAt ( j - 1 ) + res ; j -- ; } System . out . println ( res ) ; }
 }