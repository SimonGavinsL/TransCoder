class X { static void myCopy ( char s1 [ ] , char s2 [ ] , int index ) { s2 [ index ] = s1 [ index ] ; myCopy ( s1 , s2 , index + 1 ) ; }
 }