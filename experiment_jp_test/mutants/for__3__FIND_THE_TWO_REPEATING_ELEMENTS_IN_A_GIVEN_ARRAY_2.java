void printRepeating ( int arr [ ] , int size ) { int xor = arr [ 0 ] ; int set_bit_no ; int i ; int n = size - 2 ; int x = 0 , y = 0 ; set_bit_no = ( xor & ~ ( xor - 1 ) ) ; System . out . println ( " The ▁ two ▁ reppeated ▁ elements ▁ are ▁ : " ) ; System . out . println ( x + " ▁ " + y ) ; }
