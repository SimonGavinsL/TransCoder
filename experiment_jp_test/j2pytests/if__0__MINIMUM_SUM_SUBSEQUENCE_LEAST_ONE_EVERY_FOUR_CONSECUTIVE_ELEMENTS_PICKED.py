# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    dp = [ 0 ] * n
    if ( n == 1 ) :
        return arr [ 0 ]
    if ( n == 2 ) :
        return min ( arr [ 0 ] , arr [ 1 ] )
    if ( n == 3 ) :
        return min ( arr [ 0 ] , min ( arr [ 1 ] , arr [ 2 ] ) )
    if ( n == 4 ) :
        return min ( min ( arr [ 0 ] , arr [ 1 ] ) , min ( arr [ 2 ] , arr [ 3 ] ) )
    dp [ 0 ] = arr [ 0 ]
    dp [ 1 ] = arr [ 1 ]
    dp [ 2 ] = arr [ 2 ]
    dp [ 3 ] = arr [ 3 ]
    for i in range ( 4 , n ) :
        dp [ i ] = arr [ i ] + min ( min ( dp [ i - 1 ] , dp [ i - 2 ] ) , min ( dp [ i - 3 ] , dp [ i - 4 ] ) )
    return min ( min ( dp [ n - 1 ] , dp [ n - 2 ] ) , min ( dp [ n - 4 ] , dp [ n - 3 ] ) )


#TOFILL
def f_filled (arr, n):
    """ generated source for method minSum """
    dp = [None]*n
    if n == 2:
        return Math.min(arr[0], arr[1])
    if n == 3:
        return Math.min(arr[0], Math.min(arr[1], arr[2]))
    if n == 4:
        return Math.min(Math.min(arr[0], arr[1]), Math.min(arr[2], arr[3]))
    dp[0] = arr[0]
    dp[1] = arr[1]
    dp[2] = arr[2]
    dp[3] = arr[3]
    return Math.min(Math.min(dp[n - 1], dp[n - 2]), Math.min(dp[n - 4], dp[n - 3]))



if __name__ == '__main__':
    param = [
    ([2, 7, 11, 12, 13, 14, 18, 20, 22, 26, 28, 29, 31, 32, 33, 35, 38, 38, 40, 40, 41, 42, 43, 44, 45, 53, 54, 54, 59, 62, 69, 72, 74, 75, 75, 76, 79, 83, 84, 89, 91, 96, 97, 98, 99, 99],30,),
    ([50, -22, 90, -40, 46, 86, 50, 44, 12, -42, -58, 6, 52, -16, 4, 46, 44, 0, -64, 78, -14, -80, 30, -66, 78, 24, 28, 10, -72, -44, -28, -32, -30, 94, -22, 26, 16, 20, -52, -16, -80, 2, -56, -70, -76, 60, 62],40,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([63, 18, 13, 2, 1, 94, 11, 49, 82, 97, 75, 98, 25, 20, 96, 82, 60, 94, 24, 15, 79, 48, 40, 60, 9, 62, 24, 69, 31, 78, 34, 83, 22, 88],33,),
    ([-74, 16, 96],1,),
    ([0, 0, 1, 0, 1, 1],5,),
    ([2, 5, 6, 8, 10, 16, 18, 19, 20, 21, 24, 30, 34, 36, 39, 42, 52, 53, 54, 55, 56, 57, 70, 71, 72, 73, 75, 75, 77, 78, 82, 85, 87, 88, 89, 91],25,),
    ([-40, 12, -86, -54, -68, 32, 10, -24, -46, 54, -64, 20, 22, 88, 62, -4, -2, -8, -32, 88, -4, 38, 4, 86, 82, -16, -76, -44, 54, -24, -92, 74, 50, -52, 52],22,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([4, 53, 96, 86, 69, 81, 86, 95, 80, 43, 25, 66, 24, 72],12,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))