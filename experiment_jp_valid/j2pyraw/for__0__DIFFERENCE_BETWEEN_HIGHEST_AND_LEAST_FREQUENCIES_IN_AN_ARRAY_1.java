class X { static int findDiff ( int arr [ ] , int n ) { Map < Integer , Integer > mp = new HashMap < > ( ) ; int max_count = 0 , min_count = n ; for ( Map . Entry < Integer , Integer > x : mp . entrySet ( ) ) { max_count = Math . max ( max_count , x . getValue ( ) ) ; min_count = Math . min ( min_count , x . getValue ( ) ) ; } return ( max_count - min_count ) ; }
 }