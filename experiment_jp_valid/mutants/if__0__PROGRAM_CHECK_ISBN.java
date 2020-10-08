static boolean isValidISBN ( String isbn ) { int n = isbn . length ( ) ; int sum = 0 ; char last = isbn . charAt ( 9 ) ; if ( last != ' X ' && ( last < '0' || last > '9' ) ) return false ; sum += ( ( last == ' X ' ) ? 10 : ( last - '0' ) ) ; return ( sum % 11 == 0 ) ; }
