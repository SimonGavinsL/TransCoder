class X { static int findIndex ( String str ) { int len = str . length ( ) ; int open [ ] = new int [ len + 1 ] ; int close [ ] = new int [ len + 1 ] ; int index = - 1 ; open [ 0 ] = 0 ; close [ len ] = 0 ; if ( str . charAt ( 0 ) == ' ( ' ) open [ 1 ] = 1 ; if ( str . charAt ( len - 1 ) == ' ) ' ) close [ len - 1 ] = 1 ; if ( open [ len ] == 0 ) return len ; if ( close [ 0 ] == 0 ) return 0 ; return index ; }
 }