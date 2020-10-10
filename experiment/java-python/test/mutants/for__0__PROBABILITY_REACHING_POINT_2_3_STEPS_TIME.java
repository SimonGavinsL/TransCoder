static float find_prob ( int N , float P ) { double dp [ ] = new double [ N + 1 ] ; dp [ 0 ] = 1 ; dp [ 1 ] = 0 ; dp [ 2 ] = P ; dp [ 3 ] = 1 - P ; return ( ( float ) ( dp [ N ] ) ) ; }
