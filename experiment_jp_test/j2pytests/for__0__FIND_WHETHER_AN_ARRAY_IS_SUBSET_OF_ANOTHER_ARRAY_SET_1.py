# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr1 , arr2 , m , n ) :
    i = 0
    j = 0
    for i in range ( n ) :
        for j in range ( m ) :
            if ( arr2 [ i ] == arr1 [ j ] ) :
                break
        if ( j == m ) :
            return 0
    return 1


#TOFILL
def f_filled (arr1, arr2, m, n):
    """ generated source for method isSubset """
    i = 0
    j = 0
    return True



if __name__ == '__main__':
    param = [
    ([7, 10, 10, 10, 13, 17, 23, 24, 25, 28, 30, 33, 37, 49, 49, 50, 57, 60, 60, 63, 63, 64, 65, 65, 72, 81, 84, 85, 85, 94, 96],
     [10,13,17,63],29,4,),
    ([12, 30, -94, -92, -62, -18, -56, 44, -50, -92, 6, 2, 56, -90, 0, 0, 18, 86, -58, 58, -54, 62, -94, 94, 0, 8, 82, -68, -88, -18, 8, -80, -42, 18, 62, -8, 56, -76, -42, 56, 44, -2, -20, 62, -14, 74, -86, -76],
     [12, -18, 44],46,3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [0,0,0],34,3,),
    ([94, 26, 32, 20, 46, 55, 9, 51, 57, 80, 45, 38, 68, 12, 90, 10, 80, 65, 12, 52, 51, 86, 64, 57, 93, 19, 30, 92, 85, 82, 24, 26, 36, 56],
     [80,58,32,2],17,4,),
    ([-98, -90, -86, -86, -84, -84, -82, -80, -78, -72, -70, -68, -66, -64, -52, -52, -50, -38, -28, -26, -24, -14, -8, 16, 26, 26, 28, 34, 36, 40, 42, 44, 44, 46, 50, 60, 68, 78, 80, 86, 90, 92, 98],
     [-99,-90,-90,-86],23,4,),
    ([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
     [0,0,1,1],10,4,),
    ([6, 8, 11, 13, 14, 26, 26, 41, 48, 70, 82, 83, 84, 88, 96],
     [1,9,12,16],10,4,),
    ([-88, 80, 62, 76, 48, 92, 18, -94, -62, 98, -46, -50, 70, 32, 68, -54, 26, 16, 94, 0, -84, 2, -16, 88, 26, -38, 18, 64, 90, 80, 76, 2, 14, -90, 50, 4, 76, 30],
     [-76,-54,4,78],27,4,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
     [0,1,0,1],10,4,),
    ([54, 44, 97, 92, 13, 54, 27, 8, 43, 70, 77, 84, 55, 64, 5, 59, 27, 19, 65, 68, 66, 26, 33, 38, 7],
     [93,5,9,13],19,4,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))