# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , size ) :
    Hash = dict ( )
    for i in range ( size ) :
        Hash [ arr [ i ] ] = Hash.get ( arr [ i ] , 0 ) + 1 ;
    for i in Hash :
        if ( Hash [ i ] % 2 != 0 ) :
            return i
    return - 1


#TOFILL
def f_filled ( arr , n ) :
    hdict = { }
    for i in range ( n ) :
        if hdict.has_key ( arr [ i ] ) :
            val = hdict [ arr [ i ] ]
            hdict [ arr [ i ] ] = val + 1
        else :
            hdict [ arr [ i ] ] = 1
    for a in hdict.keys ( ) :
        if hdict [ a ] % 2 != 0 :
            return a
    return - 1


if __name__ == '__main__':
    param = [
    ([49, 90],1,),
    ([-96, 94, 92, -24, 48, 54, -30, -86, 28, -18, 12, -64, -36, 68, 68, -78, -6, 30, -84, 20, 52, -36, 40, -62, 90, -48, 86, 98, 12, 44, 98, -66, 52, 34, 36, 76, -50, -20, -20, -20],39,),
    ([0, 1],1,),
    ([79, 55, 18, 99, 38, 93, 19, 49, 21, 74, 16, 76, 82, 52, 86, 17, 42, 9, 6, 63, 1, 40, 75, 59, 41, 81],23,),
    ([-90, -84, -82, -68, -66, -66, -60, -60, -48, -44, -36, -34, -30, -16, -14, -12, -10, -6, 2, 10, 10, 14, 22, 26, 30, 34, 46, 50, 52, 62, 64, 64, 66, 72, 74, 78, 78, 82, 84, 88, 92],23,),
    ([1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],18,),
    ([2, 4, 5, 7, 7, 18, 18, 23, 23, 25, 25, 31, 41, 43, 45, 46, 52, 52, 55, 64, 69, 69, 80, 81, 84, 90, 91, 93, 94, 94, 94, 94, 96, 98, 99],20,),
    ([86, 66, -8, 2, -18, -22, 38, 4, -38, -54, 78, 64, 78, 20, -32, 84, -70, 66, -46, 12, -12, 8, 44, 14, 20],20,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],21,),
    ([11, 4, 98, 38, 20, 41, 1, 8],7,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))