class X { static boolean isSubsetSum ( int set [ ] , int n , int sum ) { if ( set [ n - 1 ] > sum ) return isSubsetSum ( set , n - 1 , sum ) ; return isSubsetSum ( set , n - 1 , sum ) || isSubsetSum ( set , n - 1 , sum - set [ n - 1 ] ) ; }
 }