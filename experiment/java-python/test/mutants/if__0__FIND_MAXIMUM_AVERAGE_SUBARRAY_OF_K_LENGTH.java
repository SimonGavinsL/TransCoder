static int findMaxAverage ( int [ ] arr , int n , int k ) { int [ ] csum = new int [ n ] ; csum [ 0 ] = arr [ 0 ] ; int max_sum = csum [ k - 1 ] , max_end = k - 1 ; return max_end - k + 1 ; }
