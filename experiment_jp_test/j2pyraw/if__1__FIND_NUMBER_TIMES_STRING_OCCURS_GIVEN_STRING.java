class X { static int count ( String a , String b , int m , int n ) { if ( a . charAt ( m - 1 ) == b . charAt ( n - 1 ) ) return count ( a , b , m - 1 , n - 1 ) + count ( a , b , m - 1 , n ) ; else return count ( a , b , m - 1 , n ) ; }
 }