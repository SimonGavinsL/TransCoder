# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( mat , n ) :
    flip = 0
    for i in range ( n ) :
        for j in range ( i ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                flip += 1
    return flip


#TOFILL
def f_filled ( mat , n ) :
    flip = 0
    for i in range ( n ) :
        for j in range ( i ) :
            if mat [ i ] [ j ] != mat [ j ] [ i ] :
                flip += 1
    return flip


if __name__ == '__main__':
    param = [
    ([[16, 16, 47, 49, 50, 64, 70, 83, 88], [11, 12, 24, 32, 36, 39, 48, 58, 62], [29, 31, 35, 49, 71, 78, 82, 92, 96], [6, 21, 46, 53, 83, 88, 94, 94, 97], [29, 36, 41, 52, 83, 89, 89, 90, 90], [3, 11, 35, 45, 47, 79, 81, 85, 96], [31, 43, 62, 62, 62, 65, 66, 68, 81], [8, 9, 10, 26, 36, 43, 58, 70, 95], [2, 8, 24, 31, 42, 43, 58, 90, 94]],8,),
    ([[20, 8, -42, -16, 58, 58, 80], [-28, -20, 54, 94, 62, 22, -86], [-26, 86, 48, -28, 10, 90, -40], [68, 76, 16, -50, -58, 18, -86], [40, -52, 8, -14, -8, 54, 78], [82, 92, 2, 54, 62, 80, 14], [-56, -90, 74, -16, -92, 76, 32]],6,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],38,),
    ([[66, 95, 76, 26, 11, 80, 1, 59, 16], [79, 5, 47, 12, 55, 11, 49, 12, 84], [77, 16, 8, 92, 95, 71, 16, 71, 44], [14, 17, 30, 80, 42, 42, 35, 62, 87], [47, 75, 69, 34, 25, 54, 87, 49, 62], [9, 20, 35, 98, 95, 57, 51, 64, 72], [66, 38, 22, 59, 82, 49, 40, 46, 64], [31, 15, 63, 84, 6, 18, 93, 36, 62], [96, 13, 34, 87, 16, 6, 91, 65, 13]],7,),
    ([[-94, -68, -54, -36, -32, -28, -10, 10, 30, 38, 58, 66, 78, 90], [-98, -62, -44, -38, -36, -34, -34, -26, 28, 30, 34, 64, 90, 98], [-90, -88, -84, -62, -54, -24, 4, 6, 30, 32, 40, 50, 56, 68], [-98, -80, -74, -48, -18, -14, -10, 10, 24, 42, 54, 54, 74, 96], [-84, -68, -52, -32, -16, -8, -4, 6, 44, 48, 50, 78, 80, 84], [-96, -84, -78, -42, -38, -36, -16, -14, 2, 14, 16, 24, 28, 40], [-94, -92, -86, -84, -62, -58, -52, -46, -22, -12, 16, 32, 62, 68], [-92, -72, -68, -62, -50, -50, -38, -12, 22, 40, 40, 42, 48, 70], [-90, -72, -42, -28, 16, 22, 26, 36, 42, 50, 68, 82, 90, 94], [-86, -78, -66, -60, -46, -30, -26, -20, -14, 54, 60, 66, 76, 84], [-98, -96, -76, -64, -30, -16, -4, 14, 22, 28, 48, 64, 74, 96], [-88, -68, -58, -50, -28, -16, -8, 2, 18, 20, 28, 58, 60, 82], [-94, -82, -70, 14, 14, 24, 30, 36, 48, 50, 50, 76, 78, 96], [-88, -74, -12, 6, 10, 18, 28, 46, 56, 58, 84, 90, 90, 96]],11,),
    ([[1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1]],14,),
    ([[1, 4, 11, 16, 18, 19, 20, 25, 27, 29, 30, 30, 33, 34, 35, 36, 37, 38, 40, 40, 49, 49, 51, 51, 53, 56, 57, 59, 60, 61, 61, 62, 63, 69, 72, 77, 79, 82, 85, 86, 89, 94, 97, 98], [2, 6, 8, 10, 11, 11, 11, 14, 15, 19, 20, 21, 21, 23, 26, 31, 31, 34, 37, 37, 40, 40, 41, 47, 47, 48, 52, 53, 55, 59, 67, 77, 81, 82, 82, 83, 88, 92, 92, 93, 94, 96, 97, 98], [3, 4, 4, 6, 10, 13, 13, 13, 16, 18, 24, 25, 26, 27, 28, 31, 32, 34, 35, 38, 45, 50, 52, 53, 55, 57, 57, 58, 62, 64, 65, 70, 71, 72, 75, 77, 82, 86, 86, 92, 93, 94, 98, 99], [2, 4, 5, 8, 10, 10, 13, 14, 15, 18, 19, 21, 21, 21, 24, 24, 28, 30, 30, 31, 36, 37, 38, 48, 48, 52, 53, 58, 59, 60, 61, 67, 75, 77, 77, 78, 80, 81, 86, 87, 89, 89, 96, 96], [2, 4, 8, 16, 20, 20, 24, 26, 27, 28, 29, 36, 37, 43, 43, 43, 44, 45, 46, 46, 47, 48, 49, 50, 51, 52, 56, 59, 59, 62, 70, 71, 71, 72, 73, 79, 79, 86, 86, 89, 91, 91, 91, 97], [1, 1, 2, 5, 6, 10, 17, 21, 22, 23, 23, 28, 31, 34, 36, 38, 41, 42, 43, 44, 52, 53, 54, 56, 56, 58, 59, 62, 64, 67, 67, 68, 70, 71, 77, 81, 82, 83, 83, 85, 88, 89, 90, 98], [1, 1, 2, 3, 3, 4, 6, 6, 7, 10, 11, 12, 13, 14, 15, 15, 19, 21, 25, 27, 42, 45, 46, 50, 51, 51, 52, 55, 60, 60, 67, 70, 71, 71, 77, 78, 81, 85, 86, 86, 87, 90, 95, 99], [2, 4, 7, 9, 9, 11, 15, 17, 19, 22, 27, 27, 30, 32, 34, 35, 35, 36, 41, 42, 46, 46, 48, 54, 55, 56, 59, 61, 61, 65, 66, 67, 70, 73, 80, 81, 85, 89, 90, 91, 92, 96, 96, 97], [7, 8, 12, 14, 17, 19, 21, 24, 27, 28, 34, 36, 38, 48, 54, 57, 59, 59, 62, 66, 66, 67, 70, 71, 71, 71, 72, 73, 74, 74, 76, 76, 78, 79, 80, 80, 83, 88, 88, 90, 92, 95, 96, 98], [3, 3, 8, 10, 10, 15, 16, 20, 25, 25, 25, 29, 34, 36, 42, 50, 52, 54, 56, 58, 59, 63, 64, 65, 71, 73, 73, 74, 75, 75, 76, 76, 78, 80, 82, 86, 86, 87, 87, 92, 94, 94, 96, 99], [7, 9, 12, 15, 24, 24, 25, 26, 27, 28, 32, 37, 38, 43, 44, 46, 50, 50, 52, 52, 55, 56, 56, 56, 58, 58, 59, 62, 64, 65, 68, 72, 72, 80, 85, 85, 86, 90, 91, 92, 98, 98, 98, 99], [2, 7, 9, 18, 28, 29, 31, 32, 32, 38, 39, 39, 41, 41, 45, 48, 49, 49, 49, 50, 50, 58, 58, 62, 62, 63, 68, 69, 69, 71, 72, 74, 74, 75, 77, 78, 79, 81, 82, 82, 83, 83, 95, 98], [3, 5, 6, 6, 7, 10, 10, 13, 15, 17, 22, 23, 25, 25, 25, 25, 27, 29, 35, 37, 38, 46, 47, 50, 50, 51, 53, 56, 56, 59, 71, 71, 72, 74, 77, 79, 80, 83, 84, 90, 90, 92, 95, 98], [1, 9, 19, 20, 22, 22, 22, 23, 24, 28, 32, 32, 32, 36, 36, 37, 37, 39, 45, 50, 53, 56, 58, 58, 60, 64, 66, 68, 68, 69, 72, 73, 73, 73, 75, 75, 79, 80, 80, 82, 86, 87, 91, 99], [5, 9, 12, 13, 14, 18, 23, 25, 25, 28, 29, 32, 33, 34, 39, 41, 46, 49, 50, 52, 55, 55, 56, 59, 61, 63, 65, 65, 67, 69, 69, 74, 75, 78, 80, 81, 85, 85, 86, 88, 88, 92, 96, 98], [4, 4, 9, 11, 12, 20, 23, 23, 24, 27, 33, 35, 37, 40, 41, 43, 44, 45, 45, 49, 50, 51, 54, 54, 56, 58, 63, 65, 71, 71, 72, 73, 75, 76, 76, 78, 81, 84, 86, 88, 90, 90, 96, 99], [1, 2, 8, 9, 10, 15, 17, 18, 18, 19, 20, 21, 21, 21, 26, 27, 29, 32, 33, 34, 34, 39, 44, 47, 55, 56, 58, 60, 62, 64, 65, 70, 70, 72, 74, 74, 75, 76, 79, 81, 84, 86, 90, 93], [2, 2, 6, 8, 9, 13, 15, 16, 16, 17, 18, 20, 24, 28, 33, 34, 36, 39, 40, 44, 46, 48, 50, 53, 53, 54, 61, 67, 69, 71, 72, 75, 76, 78, 83, 87, 88, 91, 93, 94, 94, 96, 97, 98], [2, 6, 9, 10, 12, 13, 14, 15, 16, 17, 21, 22, 29, 29, 31, 31, 34, 38, 38, 39, 40, 43, 44, 46, 48, 50, 52, 52, 57, 62, 65, 66, 68, 69, 69, 73, 74, 77, 79, 80, 83, 84, 87, 95], [7, 7, 13, 14, 19, 22, 24, 24, 25, 30, 30, 32, 39, 41, 43, 48, 49, 50, 50, 52, 53, 54, 58, 61, 62, 65, 65, 66, 66, 67, 69, 70, 73, 73, 75, 77, 88, 89, 92, 92, 96, 96, 97, 98], [1, 3, 3, 4, 12, 14, 27, 32, 32, 33, 33, 37, 42, 42, 42, 43, 47, 49, 53, 55, 56, 57, 59, 60, 61, 61, 61, 65, 66, 66, 67, 71, 72, 73, 78, 79, 80, 82, 87, 89, 92, 94, 95, 96], [5, 6, 6, 11, 11, 13, 18, 18, 19, 21, 25, 28, 31, 37, 40, 40, 43, 45, 51, 53, 53, 58, 63, 64, 67, 68, 73, 75, 75, 77, 82, 84, 84, 86, 88, 91, 92, 94, 94, 96, 97, 97, 98, 99], [1, 2, 3, 7, 8, 8, 8, 17, 23, 23, 24, 31, 33, 33, 36, 37, 38, 38, 43, 44, 47, 47, 47, 49, 52, 55, 56, 56, 59, 68, 71, 72, 72, 75, 79, 79, 80, 82, 83, 92, 93, 97, 97, 98], [1, 2, 6, 6, 11, 13, 15, 15, 17, 20, 20, 24, 27, 27, 28, 30, 30, 33, 36, 37, 38, 40, 40, 40, 40, 42, 46, 51, 58, 60, 64, 65, 67, 71, 72, 75, 78, 82, 85, 87, 89, 97, 98, 98], [1, 2, 3, 5, 7, 7, 7, 16, 16, 18, 20, 20, 23, 23, 32, 32, 33, 33, 34, 38, 39, 41, 42, 43, 45, 47, 47, 50, 50, 53, 53, 56, 59, 60, 61, 64, 72, 79, 79, 84, 85, 89, 94, 98], [2, 9, 11, 11, 14, 25, 26, 27, 29, 31, 32, 34, 35, 38, 38, 38, 40, 46, 47, 47, 48, 49, 51, 55, 58, 63, 63, 66, 67, 67, 68, 69, 70, 77, 80, 81, 83, 85, 89, 90, 92, 95, 97, 98], [1, 2, 5, 8, 8, 9, 12, 12, 17, 19, 20, 28, 29, 35, 38, 38, 38, 41, 43, 45, 48, 51, 56, 62, 68, 69, 70, 73, 74, 74, 77, 79, 81, 83, 84, 87, 88, 89, 92, 93, 93, 97, 98, 99], [2, 3, 4, 5, 6, 6, 10, 11, 11, 13, 14, 14, 18, 18, 19, 20, 26, 30, 31, 32, 32, 34, 34, 35, 38, 42, 43, 44, 48, 53, 55, 56, 59, 59, 65, 72, 78, 84, 85, 88, 90, 97, 97, 98], [1, 9, 10, 15, 17, 17, 18, 18, 20, 24, 25, 26, 30, 31, 33, 35, 36, 42, 43, 43, 44, 46, 46, 48, 49, 49, 49, 49, 51, 51, 52, 59, 62, 64, 65, 71, 72, 74, 79, 79, 89, 90, 94, 97], [1, 2, 10, 11, 15, 18, 18, 19, 21, 22, 25, 28, 28, 30, 37, 38, 40, 41, 46, 46, 49, 51, 52, 53, 53, 56, 64, 69, 69, 72, 72, 74, 77, 77, 77, 78, 78, 84, 85, 96, 97, 98, 98, 99], [1, 6, 6, 6, 7, 7, 10, 11, 16, 17, 18, 18, 27, 27, 33, 33, 35, 38, 41, 46, 47, 53, 54, 54, 56, 62, 63, 63, 66, 67, 67, 77, 77, 78, 79, 83, 88, 88, 89, 92, 95, 95, 96, 99], [3, 4, 6, 8, 8, 8, 10, 12, 15, 17, 19, 19, 22, 22, 25, 28, 28, 29, 34, 34, 39, 41, 42, 43, 46, 46, 46, 53, 53, 54, 56, 56, 56, 63, 64, 68, 70, 75, 82, 84, 85, 94, 95, 96], [3, 4, 4, 5, 8, 9, 17, 21, 23, 25, 31, 32, 35, 38, 38, 39, 39, 43, 49, 54, 56, 61, 61, 64, 64, 65, 65, 65, 69, 70, 70, 70, 71, 72, 74, 74, 77, 78, 78, 80, 84, 90, 96, 99], [1, 3, 6, 12, 13, 13, 13, 20, 21, 21, 24, 29, 33, 33, 38, 40, 42, 42, 45, 46, 47, 49, 55, 57, 58, 60, 60, 62, 63, 63, 67, 68, 69, 70, 72, 72, 74, 75, 75, 77, 77, 88, 95, 99], [3, 4, 4, 8, 9, 9, 9, 11, 12, 12, 15, 16, 17, 18, 20, 21, 22, 22, 25, 28, 29, 33, 34, 35, 36, 43, 46, 57, 58, 59, 63, 68, 69, 72, 76, 78, 83, 89, 90, 91, 93, 96, 97, 99], [1, 9, 11, 12, 13, 15, 19, 26, 27, 32, 34, 42, 42, 44, 48, 54, 54, 56, 57, 58, 60, 64, 76, 80, 81, 82, 82, 82, 83, 84, 85, 85, 85, 86, 87, 92, 94, 95, 96, 97, 97, 97, 98, 98], [5, 7, 16, 20, 21, 22, 27, 29, 30, 31, 32, 33, 36, 37, 38, 44, 47, 47, 50, 53, 54, 56, 58, 60, 60, 61, 62, 63, 63, 64, 64, 68, 69, 77, 81, 81, 82, 82, 84, 86, 87, 90, 92, 96], [3, 3, 6, 6, 8, 8, 9, 13, 20, 21, 27, 27, 29, 32, 34, 40, 43, 47, 49, 49, 50, 53, 54, 54, 57, 61, 63, 65, 66, 71, 72, 72, 73, 73, 74, 75, 75, 75, 79, 82, 85, 90, 92, 94], [2, 3, 5, 5, 9, 9, 14, 17, 20, 21, 23, 27, 29, 31, 33, 36, 38, 42, 43, 45, 45, 46, 47, 47, 48, 53, 54, 55, 56, 58, 60, 64, 67, 67, 69, 77, 77, 84, 87, 92, 92, 93, 94, 98], [4, 9, 10, 12, 13, 15, 16, 20, 24, 25, 26, 27, 31, 34, 38, 38, 40, 41, 43, 44, 46, 46, 47, 47, 48, 57, 64, 74, 77, 78, 79, 82, 82, 85, 87, 87, 88, 89, 91, 92, 94, 96, 97, 99], [2, 2, 4, 8, 10, 12, 13, 20, 21, 21, 29, 32, 34, 40, 40, 40, 43, 45, 46, 47, 47, 48, 49, 51, 57, 67, 68, 68, 70, 72, 76, 76, 77, 78, 79, 81, 84, 88, 89, 91, 94, 95, 97, 98], [3, 4, 4, 6, 8, 8, 9, 11, 14, 14, 15, 16, 16, 22, 22, 23, 25, 30, 30, 33, 33, 35, 36, 37, 40, 40, 42, 42, 44, 52, 55, 56, 56, 58, 60, 64, 64, 66, 67, 69, 80, 81, 81, 91], [7, 10, 10, 11, 13, 13, 13, 15, 23, 25, 27, 28, 28, 30, 34, 35, 37, 38, 39, 44, 45, 46, 49, 50, 53, 53, 56, 60, 60, 64, 64, 65, 66, 68, 68, 70, 77, 78, 79, 80, 81, 85, 92, 95], [1, 3, 7, 7, 9, 11, 12, 19, 19, 20, 22, 22, 25, 26, 34, 38, 43, 45, 47, 49, 50, 54, 55, 55, 57, 60, 62, 62, 64, 69, 70, 72, 72, 76, 77, 79, 83, 89, 93, 94, 95, 98, 99, 99]],22,),
    ([[-6]],0,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],37,),
    ([[57, 35, 39, 48, 79, 25, 49, 44, 40, 59, 90, 18, 4, 14, 32, 39, 2, 15, 34, 91, 11, 16, 23, 1, 7, 3, 40, 93, 14, 33, 51, 35, 78, 35, 67, 3, 38, 71], [57, 4, 10, 9, 40, 48, 47, 9, 33, 91, 47, 12, 66, 45, 90, 89, 94, 69, 71, 43, 83, 23, 30, 15, 52, 78, 42, 34, 65, 45, 35, 9, 48, 4, 6, 1, 40, 13], [58, 15, 43, 30, 58, 15, 58, 90, 96, 92, 80, 66, 14, 16, 79, 49, 91, 19, 1, 64, 21, 27, 41, 48, 21, 21, 21, 26, 70, 97, 63, 35, 92, 96, 61, 3, 86, 47], [92, 91, 51, 18, 77, 83, 67, 81, 77, 78, 53, 40, 53, 35, 43, 16, 39, 69, 10, 38, 19, 3, 33, 94, 60, 84, 95, 76, 23, 52, 72, 67, 14, 61, 26, 52, 81, 62], [27, 60, 67, 50, 57, 97, 65, 22, 57, 91, 71, 61, 5, 56, 59, 55, 67, 23, 89, 88, 61, 21, 70, 69, 63, 59, 36, 29, 63, 60, 82, 33, 60, 83, 24, 22, 69, 96], [89, 59, 51, 55, 68, 44, 41, 11, 19, 44, 14, 47, 14, 3, 23, 84, 76, 95, 19, 69, 67, 62, 42, 69, 43, 18, 93, 93, 6, 18, 16, 37, 28, 46, 53, 82, 5, 64], [73, 22, 7, 71, 4, 28, 4, 43, 3, 28, 82, 66, 45, 52, 59, 66, 80, 50, 84, 82, 22, 52, 98, 13, 48, 33, 58, 15, 44, 79, 91, 80, 30, 67, 72, 23, 14, 1], [70, 78, 31, 58, 42, 81, 50, 88, 23, 99, 7, 59, 1, 63, 60, 8, 69, 81, 19, 96, 61, 16, 37, 47, 69, 83, 70, 77, 72, 45, 41, 34, 78, 71, 71, 6, 94, 53], [38, 46, 91, 77, 24, 94, 98, 68, 4, 23, 30, 65, 12, 71, 20, 21, 84, 39, 83, 98, 79, 72, 76, 71, 99, 73, 27, 47, 55, 43, 4, 10, 38, 93, 14, 65, 18, 98], [66, 76, 94, 19, 66, 43, 17, 53, 69, 25, 48, 29, 70, 65, 90, 93, 6, 85, 21, 33, 12, 90, 66, 32, 14, 88, 13, 6, 12, 5, 57, 75, 87, 44, 72, 45, 66, 48], [66, 44, 52, 38, 99, 65, 41, 88, 18, 93, 96, 39, 45, 19, 35, 53, 68, 76, 14, 6, 74, 30, 18, 28, 39, 67, 20, 48, 9, 77, 25, 45, 72, 48, 36, 24, 36, 16], [14, 90, 11, 65, 5, 97, 61, 91, 5, 47, 11, 85, 83, 39, 69, 12, 76, 44, 52, 24, 35, 99, 23, 94, 56, 55, 71, 19, 3, 86, 7, 1, 44, 20, 95, 81, 77, 43], [10, 93, 48, 53, 66, 88, 68, 58, 67, 17, 7, 54, 16, 33, 46, 15, 34, 56, 84, 18, 46, 93, 54, 99, 63, 47, 28, 48, 35, 94, 77, 34, 56, 36, 43, 12, 73, 90], [8, 56, 60, 26, 78, 18, 28, 30, 65, 81, 84, 40, 74, 17, 52, 46, 28, 4, 14, 41, 2, 91, 9, 16, 85, 82, 59, 58, 63, 35, 1, 13, 48, 39, 1, 12, 31, 34], [48, 3, 7, 11, 44, 41, 4, 35, 30, 23, 86, 98, 35, 82, 72, 49, 58, 32, 71, 58, 92, 49, 88, 84, 80, 3, 86, 37, 65, 91, 12, 7, 44, 74, 50, 65, 52, 16], [27, 21, 48, 22, 70, 83, 45, 34, 84, 45, 39, 9, 33, 76, 51, 19, 82, 27, 30, 83, 93, 62, 21, 84, 13, 24, 22, 95, 86, 33, 18, 74, 88, 95, 41, 91, 51, 7], [62, 22, 26, 38, 15, 3, 28, 93, 54, 23, 46, 10, 36, 83, 66, 14, 32, 80, 73, 58, 79, 51, 34, 94, 70, 24, 7, 64, 76, 96, 3, 85, 93, 79, 12, 37, 94, 93], [33, 20, 76, 50, 37, 56, 92, 79, 66, 76, 28, 69, 38, 6, 90, 30, 51, 95, 34, 15, 40, 24, 47, 99, 50, 3, 5, 8, 50, 35, 27, 30, 44, 31, 64, 79, 13, 73], [69, 56, 99, 12, 4, 16, 97, 89, 62, 15, 41, 67, 82, 6, 20, 80, 98, 42, 78, 86, 77, 59, 21, 11, 96, 96, 34, 69, 84, 67, 91, 64, 67, 75, 50, 47, 59, 79], [82, 78, 57, 77, 3, 60, 27, 93, 26, 98, 24, 38, 49, 31, 57, 44, 23, 33, 68, 66, 26, 17, 4, 76, 11, 10, 7, 98, 73, 57, 55, 37, 41, 57, 82, 29, 80, 86], [78, 61, 89, 44, 96, 59, 79, 39, 55, 23, 94, 23, 59, 4, 37, 19, 10, 94, 72, 90, 25, 86, 50, 68, 71, 34, 56, 72, 46, 45, 28, 85, 91, 50, 34, 71, 49, 68], [46, 60, 27, 21, 44, 61, 86, 9, 64, 78, 53, 97, 30, 57, 24, 67, 38, 30, 61, 87, 79, 40, 20, 59, 31, 20, 2, 22, 96, 63, 9, 8, 81, 96, 19, 60, 97, 40], [61, 59, 30, 75, 21, 33, 92, 89, 85, 72, 98, 3, 23, 61, 87, 93, 92, 83, 9, 82, 44, 89, 68, 54, 14, 76, 49, 29, 44, 33, 94, 23, 17, 46, 45, 50, 1, 88], [53, 90, 59, 33, 63, 59, 94, 93, 7, 61, 96, 16, 51, 52, 3, 42, 9, 10, 94, 66, 14, 89, 72, 94, 99, 14, 74, 45, 78, 99, 54, 53, 80, 19, 87, 48, 12, 38], [9, 17, 96, 94, 10, 97, 46, 40, 35, 37, 16, 11, 88, 65, 94, 87, 75, 42, 16, 32, 95, 4, 54, 42, 62, 10, 90, 31, 79, 45, 42, 88, 96, 47, 88, 4, 10, 76], [1, 14, 14, 41, 6, 62, 47, 66, 23, 51, 65, 6, 16, 47, 32, 22, 93, 54, 72, 82, 40, 24, 94, 62, 25, 61, 41, 14, 95, 50, 98, 30, 65, 22, 85, 79, 3, 10], [64, 40, 52, 51, 32, 35, 71, 5, 89, 12, 91, 33, 78, 88, 39, 68, 44, 30, 5, 57, 18, 30, 58, 57, 22, 44, 12, 16, 50, 42, 80, 85, 53, 29, 5, 56, 14, 92], [35, 81, 5, 71, 97, 39, 34, 19, 78, 75, 51, 49, 39, 12, 80, 2, 90, 35, 25, 48, 87, 75, 23, 92, 33, 78, 39, 37, 70, 74, 62, 92, 12, 99, 18, 33, 89, 28], [79, 82, 20, 51, 35, 70, 24, 9, 34, 25, 27, 53, 84, 45, 31, 20, 58, 55, 12, 51, 78, 45, 48, 66, 92, 7, 93, 72, 93, 59, 70, 66, 67, 11, 10, 95, 57, 65], [56, 23, 53, 92, 41, 98, 86, 27, 56, 38, 95, 34, 5, 83, 80, 49, 10, 71, 54, 40, 81, 44, 91, 61, 96, 22, 53, 7, 60, 35, 65, 93, 2, 59, 92, 60, 80, 70], [58, 75, 10, 84, 37, 32, 71, 91, 66, 98, 51, 28, 17, 91, 45, 22, 13, 19, 93, 85, 19, 11, 66, 2, 87, 58, 24, 42, 15, 21, 95, 59, 67, 27, 39, 48, 94, 53], [48, 39, 19, 44, 34, 20, 42, 38, 95, 24, 69, 5, 12, 75, 17, 5, 72, 70, 91, 24, 20, 45, 14, 29, 43, 10, 27, 98, 93, 21, 89, 23, 40, 38, 36, 99, 90, 82], [38, 1, 96, 18, 20, 6, 20, 88, 73, 92, 41, 90, 2, 18, 78, 89, 7, 81, 34, 8, 36, 88, 60, 64, 56, 70, 53, 27, 41, 54, 35, 94, 30, 20, 90, 47, 18, 75], [49, 44, 96, 84, 67, 89, 40, 83, 21, 42, 41, 3, 19, 59, 94, 65, 56, 16, 79, 61, 59, 63, 35, 32, 2, 8, 73, 65, 87, 56, 83, 16, 85, 83, 80, 11, 92, 74], [59, 63, 9, 66, 85, 47, 15, 81, 41, 75, 3, 5, 73, 2, 99, 89, 87, 67, 10, 2, 97, 20, 57, 75, 18, 77, 66, 36, 78, 43, 5, 76, 31, 3, 87, 62, 13, 38], [68, 88, 92, 3, 70, 43, 61, 91, 7, 17, 56, 91, 74, 15, 31, 8, 17, 25, 75, 5, 55, 46, 73, 48, 21, 53, 9, 23, 45, 30, 63, 67, 29, 53, 30, 68, 58, 41], [14, 51, 22, 93, 95, 99, 28, 63, 48, 48, 31, 5, 8, 96, 86, 98, 21, 34, 16, 31, 2, 27, 25, 34, 30, 68, 27, 86, 30, 24, 25, 14, 72, 6, 28, 5, 30, 97], [93, 73, 8, 62, 72, 47, 31, 64, 16, 42, 84, 12, 40, 49, 52, 62, 96, 3, 95, 10, 35, 62, 69, 77, 31, 90, 51, 13, 91, 58, 6, 77, 5, 86, 81, 19, 76, 12]],30,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))