class X { static int findLongestRepeatingSubSeq ( char X [ ] , int m , int n ) { return dp [ m ] [ n ] = Math . max ( findLongestRepeatingSubSeq ( X , m , n - 1 ) , findLongestRepeatingSubSeq ( X , m - 1 , n ) ) ; }
 }