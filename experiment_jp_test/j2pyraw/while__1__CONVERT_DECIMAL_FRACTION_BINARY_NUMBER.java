class X { static String decimalToBinary ( double num , int k_prec ) { String binary = " " ; int Integral = ( int ) num ; double fractional = num - Integral ; binary = reverse ( binary ) ; binary += ( ' . ' ) ; return binary ; }
 }