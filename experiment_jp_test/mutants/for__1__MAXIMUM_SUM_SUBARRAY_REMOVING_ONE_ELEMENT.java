static int maxSumSubarrayRemovingOneEle ( int arr [ ] , int n ) { int fw [ ] = new int [ n ] ; int bw [ ] = new int [ n ] ; int cur_max = arr [ 0 ] , max_so_far = arr [ 0 ] ; fw [ 0 ] = arr [ 0 ] ; cur_max = max_so_far = bw [ n - 1 ] = arr [ n - 1 ] ; int fans = max_so_far ; for ( int i = 1 ; i < n - 1 ; i ++ ) fans = Math . max ( fans , fw [ i - 1 ] + bw [ i + 1 ] ) ; return fans ; }
