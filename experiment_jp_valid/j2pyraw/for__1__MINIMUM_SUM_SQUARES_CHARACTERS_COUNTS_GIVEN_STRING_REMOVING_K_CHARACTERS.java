class X { static int minStringValue ( String str , int k ) { int l = str . length ( ) ; if ( k >= l ) return 0 ; int [ ] frequency = new int [ MAX_CHAR ] ; Comparator < Integer > c = new IntCompare ( ) ; PriorityQueue < Integer > q = new PriorityQueue < > ( c ) ; while ( k != 0 ) { int temp = q . peek ( ) ; q . poll ( ) ; temp = temp - 1 ; q . add ( temp ) ; k -- ; } int result = 0 ; while ( ! q . isEmpty ( ) ) { int temp = q . peek ( ) ; result += temp * temp ; q . poll ( ) ; } return result ; }
 }