class X { static int findInteger ( int arr [ ] , int n ) { HashMap < Integer , Integer > hash = new HashMap < > ( ) ; int maximum = 0 ; for ( int i = 0 ; i < n ; i ++ ) if ( hash . get ( arr [ i ] ) > 0 ) return arr [ i ] ; return - 1 ; }
 }