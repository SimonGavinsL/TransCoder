# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    res = 0
    for i in range ( 0 , n - 1 ) :
        res = res ^ ( i + 1 ) ^ arr [ i ]
    res = res ^ arr [ n - 1 ]
    return res


#TOFILL
def f_filled ( arr , n ) :
    res = 0
    res = res ^ arr [ n - 1 ]
    return res


if __name__ == '__main__':
    param = [
    ([2, 2, 4, 5, 5, 7, 7, 7, 8, 11, 14, 15, 18, 19, 20, 25, 25, 29, 29, 31, 32, 32, 33, 38, 42, 48, 52, 55, 60, 61, 63, 71, 74, 78, 82, 82, 84, 84, 87, 87, 88, 90, 93, 94, 94],31,),
    ([46, 2, 62, 60, 92, 4, 26, 66, 66, 90, 26, -14, 76, -20, -68],8,),
    ([0, 0, 0, 1, 1, 1, 1, 1],4,),
    ([87, 67, 11, 47, 64, 81, 94, 75, 58, 77, 18, 2, 85, 26, 6, 44, 55, 19, 46, 49, 5, 69, 44, 12, 42, 66, 46, 9, 26, 49, 68, 95, 6, 9, 11, 72, 5, 67],34,),
    ([-98, -94, -92, -82, -78, -64, -62, -58, -52, -44, -40, -38, -8, 6, 10, 20, 22, 28, 30, 30, 36, 54, 54, 58, 64, 68, 76, 78, 84, 88, 90, 94, 96],29,),
    ([1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],17,),
    ([1, 14, 15, 15, 21, 34, 38, 39, 41, 50, 60, 74, 96, 97],7,),
    ([96, -12, -16, -52],3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],21,),
    ([66, 21, 21, 59, 78, 8, 46, 41, 16, 32, 97, 93, 32, 86, 91, 61, 67, 61, 97, 49, 66, 35, 24, 35, 65, 45, 83],25,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))