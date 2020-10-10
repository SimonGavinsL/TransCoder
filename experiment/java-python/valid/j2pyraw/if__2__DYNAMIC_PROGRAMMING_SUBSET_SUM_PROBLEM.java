class X { static boolean isSubsetSum ( int set [ ] , int n , int sum ) { return isSubsetSum ( set , n - 1 , sum ) || isSubsetSum ( set , n - 1 , sum - set [ n - 1 ] ) ; }
 }