class X { static int countSubarrWithEqualZeroAndOne ( int arr [ ] , int n ) { Map < Integer , Integer > um = new HashMap < > ( ) ; int curr_sum = 0 ; int count = 0 ; for ( Map . Entry < Integer , Integer > itr : um . entrySet ( ) ) { if ( itr . getValue ( ) > 1 ) count += ( ( itr . getValue ( ) * ( itr . getValue ( ) - 1 ) ) / 2 ) ; } if ( um . containsKey ( 0 ) ) count += um . get ( 0 ) ; return count ; }
 }