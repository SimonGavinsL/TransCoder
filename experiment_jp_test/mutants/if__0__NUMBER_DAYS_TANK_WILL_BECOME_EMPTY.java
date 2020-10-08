static int minDaysToEmpty ( int C , int l ) { double eq_root = ( Math . sqrt ( 1 + 8 * ( C - l ) ) - 1 ) / 2 ; return ( int ) ( Math . ceil ( eq_root ) + l ) ; }
