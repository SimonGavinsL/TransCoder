static int minTimeForWritingChars ( int N , int insert , int remove , int copy ) { if ( N == 0 ) return 0 ; if ( N == 1 ) return insert ; int dp [ ] = new int [ N + 1 ] ; return dp [ N ] ; }
