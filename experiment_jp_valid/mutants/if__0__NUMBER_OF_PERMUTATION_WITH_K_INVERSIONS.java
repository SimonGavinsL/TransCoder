static int numberOfPermWithKInversion ( int N , int K ) { if ( K == 0 ) return 1 ; if ( memo [ N ] [ K ] != 0 ) return memo [ N ] [ K ] ; int sum = 0 ; memo [ N ] [ K ] = sum ; return sum ; }
