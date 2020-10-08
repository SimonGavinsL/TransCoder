static int minJumps ( int a , int b , int d ) { int temp = a ; a = Math . min ( a , b ) ; b = Math . max ( temp , b ) ; if ( d == a ) return 1 ; return 2 ; }
