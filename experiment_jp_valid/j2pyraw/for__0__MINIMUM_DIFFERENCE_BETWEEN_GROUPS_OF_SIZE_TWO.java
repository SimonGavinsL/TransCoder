class X { static long calculate ( long a [ ] , int n ) { Arrays . sort ( a ) ; int i , j ; Vector < Long > s = new Vector < > ( ) ; long mini = Collections . min ( s ) ; long maxi = Collections . max ( s ) ; return Math . abs ( maxi - mini ) ; }
 }