static int breakSum ( int n ) { return Math . max ( ( breakSum ( n / 2 ) + breakSum ( n / 3 ) + breakSum ( n / 4 ) ) , n ) ; }
