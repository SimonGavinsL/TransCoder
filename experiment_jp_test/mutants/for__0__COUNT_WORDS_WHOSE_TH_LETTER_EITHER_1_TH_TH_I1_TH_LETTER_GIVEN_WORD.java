static int countWords ( String str , int len ) { int count = 1 ; if ( len == 1 ) return count ; if ( str . charAt ( 0 ) == str . charAt ( 1 ) ) count *= 1 ; else count *= 2 ; if ( str . charAt ( len - 1 ) == str . charAt ( len - 2 ) ) count *= 1 ; else count *= 2 ; return count ; }
