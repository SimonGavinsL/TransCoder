# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( ar , n ) :
    if ( n <= 4 ) :
        return min ( ar )
    sum = [ 0 for i in range ( n ) ]
    sum [ 0 ] = ar [ 0 ]
    sum [ 1 ] = ar [ 1 ]
    sum [ 2 ] = ar [ 2 ]
    sum [ 3 ] = ar [ 3 ]
    for i in range ( 4 , n ) :
        sum [ i ] = ar [ i ] + min ( sum [ i - 4 : i ] )
    return min ( sum [ n - 4 : n ] )


#TOFILL
def f_filled (ar, n):
    """ generated source for method minSum """
    if n <= 4:
        return Arrays.stream(ar).min().getAsInt()
    sum = [None]*n
    sum[0] = ar[0]
    sum[1] = ar[1]
    sum[2] = ar[2]
    sum[3] = ar[3]
    return Arrays.stream(Arrays.copyOfRange(sum, n - 4, n)).min().getAsInt()



if __name__ == '__main__':
    param = [
    ([4, 4, 9, 26, 31, 31, 33, 35, 40, 45, 48, 52, 57, 60, 69, 75, 82, 89, 90, 92, 95, 97],19,),
    ([60, -68, 30, -62, -8, 48, -20, 30, 16, -60, -20],5,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],43,),
    ([15, 70, 50, 28, 67, 11, 27, 42, 1, 61, 37, 8, 66, 54, 50, 91, 86, 57, 4],15,),
    ([-98, -92, -84, -80, -70, -58, -58, -48, -42, -14, -8, 24, 30, 32, 42, 62, 68, 70, 72, 88],16,),
    ([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],7,),
    ([4, 5, 5, 10, 12, 13, 16, 19, 19, 21, 22, 25, 26, 29, 30, 33, 34, 44, 46, 52, 55, 55, 56, 78, 86, 88, 88, 90, 92],16,),
    ([40, -50, -96, 78, 82, -16, 26, 8, 38, 38, 54, -24, 88, 96, -42, -84, -28, -32, -64, 74, 74, -10, -8, 66, 14, -78, 56, -22, -90, 66, -68],26,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],7,),
    ([29, 38, 20, 25, 16, 97, 16, 90, 30, 99],9,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))