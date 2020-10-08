# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    remainder = 0
    for i in range ( 0 , n ) :
        remainder = ( remainder + arr [ i ] ) % 3
    return ( remainder == 0 )


#TOFILL
def f_filled ( arr , n ) :
    remainder = 0
    return ( remainder == 0 )


if __name__ == '__main__':
    param = [
    ([2, 4, 9, 11, 12, 15, 16, 19, 21, 21, 23, 23, 24, 30, 31, 31, 32, 34, 37, 41, 41, 43, 45, 46, 47, 54, 58, 60, 62, 66, 66, 74, 74, 75, 75, 77, 77, 85, 89, 90, 92, 92, 93, 95, 98],30,),
    ([0, 66, 92, 24, -8, 88, -92, 86, 80, 82, 42, -20, -56, -2, -84, 32],14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],29,),
    ([99, 83, 11, 99, 80, 76, 32, 12, 94, 66, 76],5,),
    ([-88, -84, -80, -80, -80, -80, -72, -68, -64, -62, -60, -52, -48, -44, -36, -24, -20, -18, -14, -8, -6, -6, -4, 6, 10, 14, 18, 24, 26, 26, 50, 50, 52, 60, 76, 90, 96, 98],19,),
    ([0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],14,),
    ([6, 6, 8, 8, 10, 24, 24, 26, 27, 30, 34, 34, 36, 36, 39, 40, 41, 44, 45, 50, 52, 53, 57, 62, 64, 64, 70, 71, 72, 78, 78, 79, 80, 82, 89, 95, 96],28,),
    ([-28, -84, -14, -20, -14, -26, 28, -66, 48, 82, -46, -10, -94, 76, 56, -6, 72, -92, -32, 66, 50, -72, 64, 12, 48, 88, -36, -12, -6, -18, -36, -34, 44, 40, -54],25,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],19,),
    ([17, 47, 89, 75, 57, 69, 70, 57, 83, 79, 57, 49],8,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))