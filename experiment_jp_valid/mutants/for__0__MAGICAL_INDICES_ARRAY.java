static int solve ( int [ ] A , int n ) { int i , cnt = 0 , j ; int [ ] parent = new int [ n + 1 ] ; int [ ] vis = new int [ n + 1 ] ; for ( i = 0 ; i < n ; i ++ ) { j = i ; if ( parent [ j ] == - 1 ) { while ( parent [ j ] == - 1 ) { parent [ j ] = i ; j = ( j + A [ j ] + 1 ) % n ; } if ( parent [ j ] == i ) { while ( vis [ j ] == 0 ) { vis [ j ] = 1 ; cnt ++ ; j = ( j + A [ j ] + 1 ) % n ; } } } } return cnt ; }
