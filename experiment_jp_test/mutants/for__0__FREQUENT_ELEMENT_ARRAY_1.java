static int mostFrequent ( int arr [ ] , int n ) { Map < Integer , Integer > hp = new HashMap < Integer , Integer > ( ) ; int max_count = 0 , res = - 1 ; for ( Entry < Integer , Integer > val : hp . entrySet ( ) ) { if ( max_count < val . getValue ( ) ) { res = val . getKey ( ) ; max_count = val . getValue ( ) ; } } return res ; }
