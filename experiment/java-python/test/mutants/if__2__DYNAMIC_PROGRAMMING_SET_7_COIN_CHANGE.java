static int count ( int S [ ] , int m , int n ) { return count ( S , m - 1 , n ) + count ( S , m , n - S [ m - 1 ] ) ; }
