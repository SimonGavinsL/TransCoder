class X { static boolean isDivisible999 ( String num ) { int n = num . length ( ) ; int gSum = 0 ; if ( gSum > 1000 ) { num = Integer . toString ( gSum ) ; n = num . length ( ) ; gSum = isDivisible999 ( num ) ? 1 : 0 ; } return ( gSum == 999 ) ; }
 }