static int maxDiff ( int [ ] arr , int n ) { int result = 0 ; Arrays . sort ( arr ) ; if ( arr [ n - 2 ] != arr [ n - 1 ] ) result += Math . abs ( arr [ n - 1 ] ) ; return result ; }
