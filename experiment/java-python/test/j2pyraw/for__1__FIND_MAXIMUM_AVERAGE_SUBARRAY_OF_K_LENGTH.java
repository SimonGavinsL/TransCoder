class X { static int findMaxAverage ( int [ ] arr , int n , int k ) { if ( k > n ) return - 1 ; int [ ] csum = new int [ n ] ; csum [ 0 ] = arr [ 0 ] ; int max_sum = csum [ k - 1 ] , max_end = k - 1 ; return max_end - k + 1 ; }
 }