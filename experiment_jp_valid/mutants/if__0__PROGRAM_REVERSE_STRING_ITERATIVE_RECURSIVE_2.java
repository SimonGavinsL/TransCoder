static void recursiveReverse ( char [ ] str , int i ) { int n = str . length ; swap ( str , i , n - i - 1 ) ; recursiveReverse ( str , i + 1 ) ; }
