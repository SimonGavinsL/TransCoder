class X { public static void rearrangeArr ( int arr [ ] , int n ) { int evenPos = n / 2 ; int oddPos = n - evenPos ; int [ ] tempArr = new int [ n ] ; Arrays . sort ( tempArr ) ; int j = oddPos - 1 ; j = oddPos ; for ( int i = 0 ; i < n ; i ++ ) System . out . print ( arr [ i ] + " ▁ " ) ; }
 }