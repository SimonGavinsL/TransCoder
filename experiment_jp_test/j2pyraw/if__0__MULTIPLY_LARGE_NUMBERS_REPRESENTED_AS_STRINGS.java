class X { static String multiply ( String num1 , String num2 ) { int len1 = num1 . length ( ) ; int len2 = num2 . length ( ) ; int result [ ] = new int [ len1 + len2 ] ; int i_n1 = 0 ; int i_n2 = 0 ; int i = result . length - 1 ; while ( i >= 0 && result [ i ] == 0 ) i -- ; if ( i == - 1 ) return "0" ; String s = " " ; while ( i >= 0 ) s += ( result [ i -- ] ) ; return s ; }
 }