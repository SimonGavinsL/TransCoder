static int lcs ( int [ ] [ ] [ ] dp , int [ ] arr1 , int n , int [ ] arr2 , int m , int k ) { int ans = dp [ n ] [ m ] [ k ] ; if ( ans != - 1 ) return ans ; try { ans = Math . max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) ) ; if ( arr1 [ n - 1 ] == arr2 [ m - 1 ] ) ans = Math . max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) ) ; ans = Math . max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) ) ; } catch ( Exception e ) { } return ans ; }
