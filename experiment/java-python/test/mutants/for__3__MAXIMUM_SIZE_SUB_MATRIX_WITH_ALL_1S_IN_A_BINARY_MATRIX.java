static void printMaxSubSquare ( int M [ ] [ ] ) { int i , j ; int R = M . length ; int C = M [ 0 ] . length ; int S [ ] [ ] = new int [ R ] [ C ] ; int max_of_s , max_i , max_j ; max_of_s = S [ 0 ] [ 0 ] ; max_i = 0 ; max_j = 0 ; System . out . println ( " Maximum ▁ size ▁ sub - matrix ▁ is : ▁ " ) ; for ( i = max_i ; i > max_i - max_of_s ; i -- ) { for ( j = max_j ; j > max_j - max_of_s ; j -- ) { System . out . print ( M [ i ] [ j ] + " ▁ " ) ; } System . out . println ( ) ; } }