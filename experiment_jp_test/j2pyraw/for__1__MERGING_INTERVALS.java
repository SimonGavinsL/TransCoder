class X { public static void mergeIntervals ( Interval arr [ ] ) { Arrays . sort ( arr , new Comparator < Interval > ( ) { public int compare ( Interval i1 , Interval i2 ) { return i2 . start - i1 . start ; } } ) ; int index = 0 ; System . out . print ( " The ▁ Merged ▁ Intervals ▁ are : ▁ " ) ; }
 }