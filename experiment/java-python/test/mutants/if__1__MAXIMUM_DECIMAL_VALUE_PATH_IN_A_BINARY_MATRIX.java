static int maxDecimalValue ( int mat [ ] [ ] , int i , int j , int p ) { int result = Math . max ( maxDecimalValue ( mat , i , j + 1 , p + 1 ) , maxDecimalValue ( mat , i + 1 , j , p + 1 ) ) ; }
