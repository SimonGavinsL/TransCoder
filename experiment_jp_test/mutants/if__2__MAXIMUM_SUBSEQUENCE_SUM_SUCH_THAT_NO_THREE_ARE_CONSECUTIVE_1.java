static int maxSumWO3Consec ( int n ) { if ( n == 2 ) return sum [ n ] = arr [ 1 ] + arr [ 0 ] ; return sum [ n ] = Math . max ( Math . max ( maxSumWO3Consec ( n - 1 ) , maxSumWO3Consec ( n - 2 ) + arr [ n - 1 ] ) , arr [ n - 2 ] + arr [ n - 1 ] + maxSumWO3Consec ( n - 3 ) ) ; }
