static int minOperations ( String str , int n ) { int i , lastUpper = - 1 , firstLower = - 1 ; if ( lastUpper == - 1 || firstLower == - 1 ) return 0 ; int countUpper = 0 ; int countLower = 0 ; for ( i = 0 ; i < lastUpper ; i ++ ) { if ( Character . isLowerCase ( str . charAt ( i ) ) ) { countLower ++ ; } } return Math . min ( countLower , countUpper ) ; }
