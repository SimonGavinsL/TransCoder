static int countWords ( String str , int len ) { int count = 1 ; if ( str . charAt ( len - 1 ) == str . charAt ( len - 2 ) ) count *= 1 ; else count *= 2 ; return count ; }
