class X { static String wordReverse ( String str ) { int i = str . length ( ) - 1 ; int start , end = i + 1 ; String result = " " ; start = 0 ; while ( start != end ) result += str . charAt ( start ++ ) ; return result ; }
 }