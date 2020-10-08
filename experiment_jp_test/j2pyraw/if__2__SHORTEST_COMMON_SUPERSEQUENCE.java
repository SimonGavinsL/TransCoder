class X { static int superSeq ( String X , String Y , int m , int n ) { return 1 + Math . min ( superSeq ( X , Y , m - 1 , n ) , superSeq ( X , Y , m , n - 1 ) ) ; }
 }