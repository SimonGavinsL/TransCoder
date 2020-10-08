# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( A , B , m , n ) :
    dp = [ [ 0 for i in range ( m + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( 1 , n + 1 , 1 ) :
        for j in range ( i , m + 1 , 1 ) :
            dp [ i ] [ j ] = max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] )
    return dp [ n ] [ m ]


#TOFILL
def f_filled ( A , B , m , n ) :
    dp = [ 0 ] * ( n + 1 )
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , m + 1 ) :
            dp [ i ] [ j ] = max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] )
    return dp [ n ] [ m ]


if __name__ == '__main__':
    param = [
    ([7, 9, 22, 68],[14, 22, 54, 58],3,2,),
    ([24, 40, 98, 58, -24, 24, 76, 48, -92, -16, -46, -48, -70, 88, 66, 2, 44, 36, 34, 34, 46, 90, -80, -24, -58, 68, 72, -20, -62, -40],[30, -88, 6, -26, -76, 14, -80, -30, -58, 76, 40, -28, -54, 38, -60, -60, 88, -80, -22, 90, 50, -48, 68, -26, 26, -2, 68, -16, 88, -72],22,22,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],22,19,),
    ([32, 15, 41, 41, 4, 42, 22, 33, 33, 11, 68, 5, 41, 80, 39, 15, 36, 75, 41, 11, 25, 40, 50, 19, 39, 12, 75, 28, 52, 20, 63, 5, 27, 53, 19, 62, 98, 72, 10, 90, 74, 93, 52, 81, 91, 65, 90, 93],[80, 18, 9, 29, 62, 89, 4, 40, 47, 15, 35, 82, 22, 97, 63, 54, 7, 58, 64, 73, 54, 79, 21, 21, 20, 19, 56, 42, 6, 97, 7, 34, 55, 35, 57, 86, 73, 88, 20, 29, 48, 52, 8, 77, 2, 12, 6, 47],30,25,),
    ([-94, -76, -68, -50, -28, -20, 18, 24, 30, 54, 74, 84, 98],[-88, -80, -78, -68, -44, -38, 42, 50, 62, 68, 70, 80, 92],11,8,),
    ([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],[1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],21,33,),
    ([14, 27, 43, 49],[51, 59, 76, 83],2,2,),
    ([78, -26, -12, 38, -90],[14, 50, -6, -38, 80],3,2,),
    ([0, 1, 1, 1],[0, 0, 0, 1],3,2,),
    ([12, 69, 57, 7, 52, 14, 15, 83, 67, 57, 15, 86, 81, 43, 1, 64, 45, 68, 30, 23, 14, 70, 13, 51, 23, 33, 98, 68, 24, 43, 12, 82, 46],[12, 48, 57, 40, 47, 36, 22, 50, 68, 98, 77, 78, 39, 55, 87, 75, 65, 27, 33, 27, 70, 34, 67, 71, 84, 33, 7, 61, 3, 9, 67, 92, 60],17,32,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))