static double findMod ( double a , double b ) { double mod = a ; while ( mod >= b ) mod = mod - b ; if ( a < 0 ) return - mod ; return mod ; }
