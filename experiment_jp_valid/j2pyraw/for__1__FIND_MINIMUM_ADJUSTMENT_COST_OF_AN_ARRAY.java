class X { static int minAdjustmentCost ( int A [ ] , int n , int target ) { int [ ] [ ] dp = new int [ n ] [ M + 1 ] ; int res = Integer . MAX_VALUE ; for ( int j = 0 ; j <= M ; j ++ ) res = Math . min ( res , dp [ n - 1 ] [ j ] ) ; return res ; }
 }