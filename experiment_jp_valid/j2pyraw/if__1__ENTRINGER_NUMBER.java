class X { static int zigzag ( int n , int k ) { return zigzag ( n , k - 1 ) + zigzag ( n - 1 , n - k ) ; }
 }