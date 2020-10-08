static int countStrings ( int n ) { int a [ ] = new int [ n ] , b [ ] = new int [ n ] ; a [ 0 ] = b [ 0 ] = 1 ; from 2 ^ n return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ] ; }
