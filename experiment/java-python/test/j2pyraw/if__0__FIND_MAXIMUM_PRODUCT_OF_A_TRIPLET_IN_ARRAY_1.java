class X { static int maxProduct ( int arr [ ] , int n ) { Arrays . sort ( arr ) ; return Math . max ( arr [ 0 ] * arr [ 1 ] * arr [ n - 1 ] , arr [ n - 1 ] * arr [ n - 2 ] * arr [ n - 3 ] ) ; }
 }