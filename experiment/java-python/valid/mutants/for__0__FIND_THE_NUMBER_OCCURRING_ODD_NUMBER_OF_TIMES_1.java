static int getOddOccurrence ( int arr [ ] , int n ) { HashMap < Integer , Integer > hmap = new HashMap < > ( ) ; for ( Integer a : hmap . keySet ( ) ) { if ( hmap . get ( a ) % 2 != 0 ) return a ; } return - 1 ; }