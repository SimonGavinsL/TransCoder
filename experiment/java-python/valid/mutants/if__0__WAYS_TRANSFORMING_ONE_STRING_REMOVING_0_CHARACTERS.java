static int countTransformation ( String a , String b ) { int n = a . length ( ) , m = b . length ( ) ; int dp [ ] [ ] = new int [ m + 1 ] [ n + 1 ] ; return dp [ m - 1 ] [ n - 1 ] ; }
