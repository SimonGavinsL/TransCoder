class X { static int printCountRec ( int dist ) { return printCountRec ( dist - 1 ) + printCountRec ( dist - 2 ) + printCountRec ( dist - 3 ) ; }
 }