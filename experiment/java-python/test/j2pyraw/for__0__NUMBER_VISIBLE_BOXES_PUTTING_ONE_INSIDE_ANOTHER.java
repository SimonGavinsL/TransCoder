class X { static int minimumBox ( int [ ] arr , int n ) { Queue < Integer > q = new LinkedList < > ( ) ; Arrays . sort ( arr ) ; q . add ( arr [ 0 ] ) ; return q . size ( ) ; }
 }