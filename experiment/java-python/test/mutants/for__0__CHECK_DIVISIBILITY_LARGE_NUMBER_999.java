static boolean isDivisible999 ( String num ) { int n = num . length ( ) ; if ( n == 0 && num . charAt ( 0 ) == '0' ) return true ; if ( n % 3 == 1 ) num = "00" + num ; if ( n % 3 == 2 ) num = "0" + num ; int gSum = 0 ; if ( gSum > 1000 ) { num = Integer . toString ( gSum ) ; n = num . length ( ) ; gSum = isDivisible999 ( num ) ? 1 : 0 ; } return ( gSum == 999 ) ; }