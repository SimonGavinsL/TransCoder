static boolean isConvertible ( String str1 , String str2 , int k ) { if ( ( str1 . length ( ) + str2 . length ( ) ) < k ) return true ; int commonLength = 0 ; if ( ( k - str1 . length ( ) - str2 . length ( ) + 2 * commonLength ) % 2 == 0 ) return true ; return false ; }
