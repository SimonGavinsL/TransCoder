class X { static int countFriendsPairings ( int n ) { if ( n > 2 ) return dp [ n ] = countFriendsPairings ( n - 1 ) + ( n - 1 ) * countFriendsPairings ( n - 2 ) ; else return dp [ n ] = n ; }
 }