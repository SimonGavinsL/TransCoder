static int lis ( int [ ] arr , int n ) { int [ ] mpis = new int [ n ] ; int max = Integer . MIN_VALUE ; for ( int k = 0 ; k < mpis . length ; k ++ ) { if ( mpis [ k ] > max ) { max = mpis [ k ] ; } } return max ; }
