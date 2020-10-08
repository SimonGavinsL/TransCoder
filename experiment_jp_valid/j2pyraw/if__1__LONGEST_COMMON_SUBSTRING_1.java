class X { static int lcs ( int i , int j , int count ) { count = Math . max ( count , Math . max ( lcs ( i , j - 1 , 0 ) , lcs ( i - 1 , j , 0 ) ) ) ; return count ; }
 }