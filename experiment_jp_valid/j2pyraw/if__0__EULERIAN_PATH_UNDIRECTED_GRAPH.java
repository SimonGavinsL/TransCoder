class X { static void findpath ( int [ ] [ ] graph , int n ) { Vector < Integer > numofadj = new Vector < > ( ) ; int startPoint = 0 , numofodd = 0 ; Stack < Integer > stack = new Stack < > ( ) ; Vector < Integer > path = new Vector < > ( ) ; int cur = startPoint ; while ( ! stack . isEmpty ( ) || accumulate ( graph [ cur ] , 0 ) != 0 ) { if ( accumulate ( graph [ cur ] , 0 ) == 0 ) { path . add ( cur ) ; cur = stack . pop ( ) ; } else { for ( int i = 0 ; i < n ; i ++ ) { if ( graph [ cur ] [ i ] == 1 ) { stack . add ( cur ) ; graph [ cur ] [ i ] = 0 ; graph [ i ] [ cur ] = 0 ; cur = i ; break ; } } } } System . out . println ( cur ) ; }
 }