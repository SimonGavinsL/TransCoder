# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( gold , m , n ) :
    goldTable = [ [ 0 for i in range ( n ) ] for j in range ( m ) ]
    for col in range ( n - 1 , - 1 , - 1 ) :
        for row in range ( m ) :
            if ( col == n - 1 ) :
                right = 0
            else :
                right = goldTable [ row ] [ col + 1 ]
            if ( row == 0 or col == n - 1 ) :
                right_up = 0
            else :
                right_up = goldTable [ row - 1 ] [ col + 1 ]
            if ( row == m - 1 or col == n - 1 ) :
                right_down = 0
            else :
                right_down = goldTable [ row + 1 ] [ col + 1 ]
            goldTable [ row ] [ col ] = gold [ row ] [ col ] + max ( right , right_up , right_down )
    res = goldTable [ 0 ] [ 0 ]
    for i in range ( 1 , m ) :
        res = max ( res , goldTable [ i ] [ 0 ] )
    return res


#TOFILL
def f_filled (gold, m, n):
    """ generated source for method getMaxGold """
    goldTable = [None]*m
    res = goldTable[0][0]
    return res



if __name__ == '__main__':
    param = [
    ([[19, 20, 23, 25, 28, 35, 35, 40, 45, 46, 48, 54, 57, 59, 74, 76, 78, 82, 84, 86, 87, 90, 91, 96], [9, 13, 17, 20, 26, 27, 42, 46, 48, 62, 67, 69, 72, 73, 76, 77, 82, 83, 86, 93, 95, 95, 98, 98], [2, 12, 18, 25, 29, 30, 31, 33, 39, 45, 48, 49, 56, 57, 60, 61, 64, 72, 73, 78, 79, 94, 98, 98], [2, 3, 10, 15, 20, 22, 23, 23, 27, 29, 36, 40, 42, 46, 48, 53, 53, 60, 60, 70, 73, 78, 98, 98], [6, 10, 11, 12, 15, 20, 28, 28, 33, 40, 43, 48, 51, 57, 60, 60, 61, 62, 66, 68, 72, 75, 92, 97], [2, 11, 12, 14, 15, 19, 21, 26, 30, 35, 36, 36, 46, 51, 56, 63, 69, 74, 82, 88, 89, 89, 89, 94], [1, 4, 5, 10, 11, 13, 15, 18, 23, 28, 44, 53, 53, 66, 67, 69, 70, 71, 71, 77, 79, 87, 88, 99], [2, 2, 5, 7, 7, 8, 9, 17, 26, 30, 35, 39, 41, 43, 49, 63, 64, 65, 70, 70, 80, 89, 96, 99], [4, 7, 11, 12, 14, 16, 20, 21, 27, 41, 42, 42, 43, 48, 49, 52, 62, 66, 75, 76, 81, 86, 97, 99], [1, 12, 13, 15, 17, 19, 26, 34, 47, 47, 47, 48, 51, 52, 53, 60, 61, 63, 64, 74, 77, 82, 87, 93], [1, 2, 4, 8, 14, 19, 22, 24, 31, 31, 37, 54, 60, 63, 66, 68, 76, 80, 80, 84, 88, 92, 93, 99], [1, 2, 3, 6, 7, 9, 11, 19, 25, 27, 35, 36, 45, 52, 57, 57, 86, 88, 89, 89, 93, 94, 97, 99], [7, 8, 9, 10, 11, 30, 33, 34, 37, 48, 50, 50, 56, 60, 66, 70, 72, 73, 76, 79, 86, 88, 95, 95], [1, 4, 5, 5, 6, 11, 26, 27, 32, 36, 43, 47, 47, 47, 50, 56, 56, 66, 76, 78, 78, 94, 97, 99], [6, 15, 18, 27, 36, 38, 40, 44, 47, 48, 64, 64, 68, 70, 76, 79, 83, 85, 86, 90, 93, 93, 95, 97], [1, 4, 4, 10, 11, 12, 16, 19, 20, 22, 22, 23, 35, 49, 51, 58, 66, 66, 68, 76, 77, 81, 86, 94], [2, 9, 12, 12, 13, 20, 20, 35, 44, 48, 51, 55, 62, 66, 71, 71, 73, 74, 78, 83, 89, 90, 93, 99], [9, 15, 20, 24, 25, 31, 32, 35, 36, 49, 50, 51, 52, 55, 58, 63, 79, 79, 85, 89, 90, 96, 98, 99], [6, 10, 12, 15, 16, 17, 17, 21, 24, 44, 48, 53, 58, 60, 61, 64, 67, 74, 81, 84, 86, 87, 88, 92], [7, 10, 14, 20, 21, 27, 30, 30, 31, 34, 36, 37, 39, 45, 55, 55, 63, 64, 66, 82, 88, 88, 94, 95], [6, 11, 13, 21, 22, 23, 23, 24, 28, 35, 36, 40, 41, 53, 55, 57, 63, 66, 73, 74, 77, 78, 87, 96], [4, 17, 19, 23, 25, 38, 42, 45, 50, 57, 61, 62, 62, 62, 62, 64, 75, 78, 79, 79, 82, 85, 86, 93], [14, 15, 21, 27, 38, 39, 40, 42, 43, 43, 50, 51, 54, 58, 58, 59, 60, 62, 63, 70, 75, 85, 91, 92], [6, 7, 11, 12, 20, 30, 40, 41, 41, 44, 47, 51, 52, 53, 59, 75, 76, 77, 84, 87, 91, 93, 95, 97]],23,21,),
    ([[38, 12, 92, -6, 8], [80, 66, -56, -54, -74], [36, 6, 52, -78, -92], [80, 76, 88, 10, -30], [32, 64, 18, 58, -2]],2,3,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],33,35,),
    ([[45, 96, 71], [87, 80, 90], [96, 72, 49]],1,1,),
    ([[-98, -98, -92, -82, -80, -72, -70, -48, -38, -32, -32, -28, -16, -2, 0, 0, 20, 20, 24, 30, 36, 40, 46, 58, 62, 62, 66, 74, 74, 76, 80, 82], [-96, -94, -94, -88, -80, -64, -54, -48, -46, -44, -38, -36, -34, -32, -30, -30, -24, -16, 2, 8, 26, 36, 36, 40, 48, 52, 78, 80, 80, 80, 88, 94], [-98, -98, -92, -88, -88, -88, -62, -60, -46, -34, -24, -16, -14, 8, 10, 16, 18, 20, 30, 44, 48, 48, 50, 54, 54, 70, 70, 76, 78, 82, 84, 94], [-94, -80, -76, -74, -66, -58, -48, -38, -26, -16, -12, -10, -8, -2, 0, 8, 10, 10, 12, 22, 28, 32, 40, 42, 44, 50, 60, 72, 84, 86, 90, 94], [-88, -72, -62, -46, -44, -44, -34, -30, -28, -28, -18, -18, -10, -6, -4, -2, 2, 8, 8, 22, 32, 34, 38, 46, 54, 54, 54, 76, 76, 80, 84, 86], [-94, -94, -82, -80, -78, -70, -58, -46, -36, -28, -10, -10, 0, 2, 2, 4, 8, 14, 24, 32, 34, 34, 38, 42, 42, 42, 58, 84, 86, 88, 94, 96], [-98, -96, -96, -88, -80, -68, -62, -54, -52, -28, -28, -26, -22, -12, -8, -4, 2, 8, 16, 16, 28, 30, 32, 38, 54, 58, 66, 70, 74, 76, 96, 98], [-86, -84, -80, -62, -62, -58, -52, -50, -42, -38, -36, -36, -28, -18, -4, 10, 14, 38, 40, 46, 46, 48, 54, 72, 72, 74, 84, 86, 86, 88, 90, 96], [-78, -74, -66, -62, -48, -26, -18, -12, 6, 8, 18, 22, 24, 34, 36, 38, 42, 46, 64, 66, 66, 68, 70, 72, 76, 76, 78, 80, 84, 86, 88, 90], [-98, -98, -92, -84, -74, -70, -68, -50, -50, -48, -48, -36, -30, -6, -4, -4, -4, 10, 24, 28, 30, 32, 50, 58, 60, 62, 76, 78, 84, 90, 90, 98], [-98, -96, -82, -78, -74, -62, -62, -60, -58, -56, -50, -42, -36, -32, -20, -4, 0, 2, 6, 14, 16, 26, 26, 42, 46, 70, 70, 72, 78, 82, 86, 90], [-86, -80, -80, -76, -70, -66, -58, -54, -50, -44, -42, -36, -32, -24, -22, -16, -8, -6, 2, 4, 16, 18, 36, 40, 46, 52, 58, 60, 62, 74, 76, 98], [-86, -78, -66, -64, -58, -52, -38, -32, -30, -28, -18, -18, -16, -10, -8, 2, 2, 4, 6, 6, 14, 22, 36, 36, 42, 52, 54, 76, 78, 84, 88, 98], [-98, -94, -94, -74, -72, -52, -50, -38, -30, -26, -16, -14, -4, 2, 2, 4, 4, 16, 22, 24, 28, 32, 34, 34, 36, 50, 56, 66, 68, 80, 82, 94], [-98, -90, -86, -78, -74, -72, -70, -58, -56, -52, -50, -44, -30, -24, -24, -2, 0, 6, 20, 32, 40, 40, 46, 48, 50, 58, 64, 74, 84, 90, 90, 90], [-98, -92, -86, -84, -82, -82, -78, -66, -64, -50, -40, -24, -24, -22, -22, -14, -12, -8, 0, 8, 12, 14, 20, 26, 42, 42, 58, 64, 82, 86, 92, 96], [-98, -90, -86, -76, -68, -64, -64, -64, -54, -54, -52, -44, -34, -34, -12, 6, 10, 12, 26, 38, 40, 40, 60, 68, 68, 68, 74, 78, 80, 88, 98, 98], [-92, -92, -68, -60, -54, -52, -48, -46, -40, -36, -32, -30, -28, -24, -24, -18, -4, -2, 2, 28, 32, 38, 42, 46, 60, 62, 72, 78, 80, 82, 82, 90], [-98, -86, -80, -80, -76, -64, -62, -60, -50, -34, -22, -18, -14, -12, -12, -10, 2, 6, 10, 18, 22, 28, 32, 32, 36, 38, 48, 66, 72, 82, 90, 96], [-92, -90, -86, -84, -82, -78, -72, -72, -68, -68, -60, -46, -38, -30, -28, 2, 8, 10, 18, 22, 24, 28, 40, 40, 52, 54, 64, 74, 80, 82, 86, 96], [-96, -86, -82, -82, -70, -70, -62, -62, -58, -58, -56, -56, -52, -52, -46, -42, -38, -34, -26, -24, -6, -6, -2, 8, 22, 26, 38, 52, 70, 74, 82, 90], [-92, -70, -64, -62, -56, -54, -48, -42, -36, -22, -22, -20, -14, -14, -2, 2, 2, 12, 22, 26, 60, 64, 68, 70, 70, 74, 74, 80, 84, 88, 88, 90], [-98, -98, -84, -84, -84, -80, -64, -60, -54, -54, -44, -34, -30, -18, -16, -14, 2, 8, 10, 28, 30, 32, 50, 58, 62, 62, 64, 72, 78, 78, 82, 88], [-96, -94, -86, -86, -60, -56, -52, -50, -34, -26, -14, -10, -6, -4, 2, 18, 20, 30, 38, 40, 42, 46, 48, 52, 54, 66, 68, 74, 74, 84, 92, 98], [-98, -96, -96, -94, -66, -50, -44, -44, -38, -30, -30, -22, -20, -18, -16, -14, -14, -4, -4, -2, 2, 22, 30, 42, 52, 54, 60, 70, 80, 84, 92, 96], [-96, -84, -80, -78, -76, -74, -68, -64, -60, -58, -54, -46, -26, -14, -14, -10, -2, 4, 10, 10, 12, 26, 28, 28, 38, 40, 42, 42, 50, 82, 88, 88], [-90, -78, -78, -76, -76, -76, -64, -64, -62, -44, -40, -32, -28, -24, -10, 4, 24, 28, 30, 44, 58, 60, 62, 72, 74, 76, 76, 78, 80, 82, 82, 90], [-88, -86, -72, -66, -60, -60, -58, -58, -54, -38, -32, -30, -16, -14, -10, -10, -6, 0, 8, 12, 16, 20, 22, 26, 30, 34, 36, 44, 52, 64, 66, 88], [-98, -94, -92, -92, -88, -68, -64, -64, -62, -44, -44, -36, -32, -32, -24, -18, -16, -6, -6, 6, 8, 14, 20, 26, 28, 36, 38, 40, 56, 56, 66, 84], [-98, -94, -92, -90, -58, -56, -44, -42, -40, -40, -36, -32, -32, -12, -10, -2, -2, -2, 0, 8, 16, 18, 26, 26, 42, 46, 52, 54, 84, 86, 88, 94], [-80, -78, -78, -70, -58, -56, -56, -36, -34, -32, -6, 4, 6, 10, 20, 32, 40, 42, 54, 58, 58, 64, 66, 66, 66, 66, 80, 82, 82, 82, 88, 90], [-92, -90, -78, -74, -70, -50, -48, -46, -46, -40, -40, -36, -24, -22, -20, -10, -10, -8, -8, -4, 6, 14, 20, 32, 38, 46, 46, 48, 60, 68, 68, 74]],29,31,),
    ([[1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0], [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1]],23,17,),
    ([[13, 26, 41, 59, 89, 95, 99], [5, 21, 27, 30, 41, 84, 92], [6, 46, 75, 76, 95, 96, 97], [13, 21, 33, 62, 74, 85, 88], [2, 3, 15, 25, 56, 73, 97], [38, 65, 71, 76, 82, 86, 86], [2, 28, 32, 51, 73, 77, 90]],4,4,),
    ([[10, -88, 60, -18, -24, -72, -10, 8, -12, 16, -22, -94, 12, -8, 66, 10, 6, 6, 52, -6, -18, 98, 44, 48, -38, -32, -84, -56, -52, -60, -6, -74, -54, 76, -74, -36, -44, 94, -52, 74, 14], [0, -12, -26, -24, -72, 28, -72, -44, 32, -28, -98, -64, -48, 72, -74, -10, 10, -44, 30, -12, -26, -38, -14, 72, -42, 68, 26, 78, -6, -58, -70, 74, 24, -68, -22, 48, 14, 86, -14, 58, -52], [48, -18, 34, -38, 8, 96, -22, 14, -48, 74, 58, -70, -30, -40, -12, -90, 8, -98, -56, 60, 46, 38, -82, 32, -24, -68, -92, 72, 2, -96, -96, 72, 38, 38, 12, -18, -36, -94, -68, -32, 54], [-28, 4, -84, -68, -56, -60, -12, 82, 2, 14, -2, 62, 42, 36, 56, -12, -30, -72, -70, 10, 96, -84, -44, 64, 2, 70, -78, -62, -48, -94, 48, 28, -78, 64, -4, 80, -34, 4, 68, -18, -48], [-38, 0, 34, 28, 80, -36, -4, 52, -86, 84, 44, 16, 34, 8, -38, -80, -62, -78, 62, 50, 98, -88, -40, -66, -16, -20, -34, -84, 48, -28, -4, -10, 34, -10, 52, -58, -92, -46, 14, -86, 66], [-8, -56, -18, 64, -64, -82, 14, -60, -4, -32, -52, -70, 62, 56, -58, -26, -32, 84, 88, 28, -34, -56, 12, 56, 54, 92, -90, 8, 84, 18, 12, 40, -80, -24, 66, -22, -14, 76, -46, -18, 10], [-22, -34, -92, -58, -6, -26, 26, 30, -92, 82, 12, -60, -60, -10, 24, 78, -78, 50, -6, 10, -32, -10, -6, 72, -90, -54, -32, -88, -86, 30, 70, -4, 84, -40, -52, 32, -46, -92, -18, -92, -16], [-78, 0, 56, -10, 14, 64, 84, -6, -32, -54, 42, -22, 26, -94, 32, 54, -32, 20, -76, 6, -68, -72, -54, 32, 14, -36, -2, -74, 44, 76, 28, -34, 20, 84, 56, -60, -6, 30, -4, 36, 54], [90, -48, -22, 20, 26, 48, -64, 88, 20, 46, -86, -92, 2, 24, -4, 4, -36, -12, 28, -38, -84, 48, -46, -30, 68, -8, -30, -10, -2, 64, -4, -30, 48, 2, 96, 26, -76, -26, 14, -94, 86], [-92, -66, -14, 94, -92, -2, 30, -8, 88, 34, -52, 60, 52, -10, -18, 28, 2, 94, -12, 62, -48, 30, 22, -26, 70, -84, -4, 82, -42, 32, 62, 30, -54, 80, -34, 32, -94, -8, -40, -28, 32], [-28, 26, 2, 86, -74, 8, -38, 84, -6, 18, -38, 48, -60, 36, -58, 12, -76, 62, -4, -14, -18, -74, -56, -16, 48, 74, -46, 12, -42, -18, 62, 18, 98, -80, -92, 22, -80, -74, 10, -72, -88], [12, 54, 48, 60, 32, -74, 54, 50, 32, -38, 96, 20, 72, -32, 76, -30, 96, 58, -2, 40, 12, 72, 94, 82, 70, 74, -90, -82, -2, 6, 2, -18, -34, -58, -66, 12, 72, 68, -76, -42, -4], [-60, -30, 70, 42, -52, 4, 32, 20, -40, -34, 26, -74, 36, -10, -16, 0, 16, -66, 4, -46, -54, -50, -76, 52, -4, -96, 60, -62, 82, 8, 56, 70, 32, -44, -68, -8, -10, -42, 44, 84, 28], [-8, 94, 98, 78, 38, 8, 22, -6, 96, -8, 48, 26, -22, 12, -46, 92, 80, 12, 62, 4, 80, -20, 16, -28, 70, -88, 44, 68, 22, 8, 6, 84, 98, 4, -68, -44, -4, 94, 40, 38, 32], [54, 80, -38, 14, -36, -96, 28, -86, -36, -42, 34, 22, 16, 8, 22, 36, -24, -32, 78, 36, 12, -10, -50, 8, 56, -74, -92, -64, -74, 86, 28, 38, 48, 20, 82, 60, -10, 32, -60, 58, -52], [6, 18, -12, -80, -42, -12, -34, -38, 16, 42, 98, 6, 40, -28, 90, 76, 94, -36, 74, 0, -52, -52, 24, 0, 78, 44, 2, -94, 72, 96, 8, 64, -40, -42, -2, -80, 52, -86, 58, -72, -10], [-2, -38, 56, 24, 44, 50, 58, -56, 96, -96, 56, -72, -86, 68, 58, -32, 48, 24, -68, -66, 64, 0, -82, -14, 30, 4, -8, -8, 22, -38, -4, -78, -50, 90, -72, -2, -66, 50, -60, 26, -10], [42, -54, 82, -20, -94, 32, 6, -58, 62, 86, 66, -10, 0, 78, -14, 66, -74, 38, -42, -2, -42, -66, -52, -38, 38, 32, -16, 78, 80, 40, -98, -98, -62, -36, 18, 8, 12, -20, 94, -92, 52], [48, -80, 76, -36, 90, 6, -30, -22, 10, -6, 42, -86, -52, 84, -86, -12, -92, -72, 78, 28, -98, 38, 80, 76, 18, 64, 66, -8, -6, -66, -92, 86, -26, -98, -88, 62, 82, -8, -34, -64, 44], [-26, -28, 92, -82, -36, -24, -58, 32, 44, -70, 2, -72, 54, -64, 58, 92, -36, -14, -22, -70, -30, -10, -84, -22, 82, 88, -18, 24, -18, -22, 4, 72, 28, -46, 48, -14, 92, 24, -82, 92, 40], [-32, -60, -32, 72, 98, -96, 34, -86, -92, -4, -52, -52, 18, -56, -36, -34, -22, -28, 72, 54, -20, -42, 64, 0, 26, 34, -20, -6, -80, -48, 22, 12, -58, 2, 58, -2, -34, 92, -34, 32, 40], [70, 60, -76, -54, -76, 56, -78, 44, 42, -78, -40, 12, 50, 46, 48, -12, 62, -46, -4, -62, 24, -10, 54, 76, 22, 4, 26, 96, -82, -88, -72, 48, -18, 16, -22, 48, 0, -32, 82, 76, 96], [38, -80, -92, 14, 2, -92, 62, 98, -34, -30, -32, -32, 72, -12, -12, 30, -24, -76, -58, -24, -80, 48, -22, 54, -80, 64, -90, -26, 56, -46, 18, -70, 96, 86, 68, -72, 52, 28, -98, -42, 90], [-20, -66, 94, 20, 14, -82, 94, 60, 92, 46, -86, 18, -44, 42, 96, 40, 90, -96, -10, 44, -54, -50, 10, -48, 78, 66, -62, 42, -88, -58, 80, 36, -20, 70, 82, -12, -90, 14, -94, 8, 90], [40, 54, 2, 12, -98, -96, 48, -10, -64, -16, 22, 98, -98, 76, -28, 76, 66, 56, -10, -34, 44, 14, 86, 94, 50, -18, -76, -46, 30, 94, 42, -70, -72, -48, 48, -88, 94, 50, 84, -64, 24], [-14, -96, 94, -42, 94, 52, 58, 62, 46, 14, -28, -68, 42, -80, 70, -44, -94, -66, 54, -60, -58, 30, 40, -30, 78, -76, -40, 24, 98, 6, -42, 72, 20, 64, -84, -30, 84, -34, -16, -86, 70], [-20, -66, 90, 0, 58, -12, -14, -98, -68, -12, 82, 0, 60, 94, -10, 96, 62, -66, -22, 84, -20, -56, -60, 98, -18, 96, 10, 48, 2, 52, -64, -70, 8, -88, -20, -50, 56, -10, 72, -30, -68], [-32, 66, 70, 82, -30, 24, 58, 0, -80, -96, 18, -44, 82, 76, -10, 34, -34, 38, -30, -88, -68, 2, 16, 4, -22, 36, 58, -56, 48, 70, 46, 24, -86, -94, 2, 6, -70, -68, -82, -20, 30], [44, 90, 0, 98, 94, -34, -8, 66, 80, -98, 32, -26, 96, -98, 14, 22, 74, -62, -4, -52, 44, -62, -6, 26, 86, -18, 88, -20, 4, 72, -10, 4, 34, 4, -36, -76, 8, 80, -84, -50, 14], [40, -16, 96, 22, -26, 18, -18, 78, -72, -84, -10, -42, 18, 4, 26, 0, 70, -84, 84, -68, 54, -16, -34, 32, -28, 86, -8, 40, 90, -92, -78, 16, -78, 84, -8, -28, -12, -44, 10, -10, -42], [98, 72, 68, -4, 68, 68, 66, 34, 52, -58, 12, 2, -62, 64, -40, 42, 60, -88, -72, -20, -46, 46, 94, 32, -72, -92, -56, -98, -64, 66, -70, -42, -44, -88, -92, 10, 50, -26, -40, -70, 84], [-58, 84, -40, -16, -72, 10, -26, 76, -72, -14, 50, 16, 6, 6, -8, -82, 96, -80, -70, 46, 66, -46, 96, 68, -50, 54, 4, -32, 32, 62, -80, 36, 88, 88, 74, -22, -80, 8, 98, 62, -42], [50, -68, 82, -28, 72, -78, 82, -84, 80, -2, -94, -46, -16, 16, -64, -12, -38, -84, 98, -68, -74, 14, 88, -66, -50, 58, 98, 70, -34, -4, 86, 28, 60, -34, -52, -22, 12, 40, 98, 42, 66], [90, -58, -18, -70, -12, -86, 2, 26, 70, -76, 80, -38, 68, -30, -62, -2, 0, 88, -62, -44, 84, 32, 98, 28, -42, 80, 28, 80, -70, 2, 80, 74, 92, 72, 56, -14, 28, -52, -28, -50, 0], [-52, -46, 30, 6, -10, 76, 60, -34, -38, -58, 12, 58, -50, 82, -40, -16, 14, 94, 84, -22, -36, 22, 14, 84, -38, 62, 70, -34, -30, -18, 46, -82, -18, 96, -14, -58, 16, 96, -76, -60, 50], [68, 74, 10, -20, 14, -62, -70, -86, -36, 90, 44, -12, 74, -4, -34, -16, 84, -66, -20, 86, 52, 88, 6, 64, 60, 4, -10, -90, -48, 82, -26, 14, 36, -44, 38, 34, -86, -80, 90, 8, -70], [-60, 56, -54, 10, -82, 66, 14, -16, -46, -88, 96, -58, 4, 44, 74, 32, 22, 44, 94, 48, -96, -74, -2, -90, 32, 62, 36, 56, -10, 10, 84, -64, 54, -32, -42, 36, -32, 14, -86, -98, 10], [98, -62, 76, -38, 36, 20, 72, -18, 2, -18, -66, 16, -66, 28, -8, -44, 98, -12, 12, -94, 38, 38, -6, -40, 66, -34, 16, -96, -60, 24, -50, 96, -58, -26, 74, -48, 72, -26, -38, 28, 82], [-60, -62, 24, -74, 72, 22, 56, 78, -56, -10, 86, -60, 54, -92, 18, 36, -26, 66, -18, 54, 50, -70, -10, 20, -4, -6, -34, 80, -76, -10, 76, -72, -6, -44, -64, 88, 78, 78, -8, -26, 2], [-28, -98, -50, 18, 8, -16, 16, 58, 4, 28, 14, 76, 96, 56, 56, -86, 14, -56, 74, -28, -34, 30, 74, 30, 72, 18, 42, -64, -94, 54, -14, -42, 80, 40, -94, -36, -32, -70, 18, -26, 86], [28, 6, -82, 6, -2, -26, 6, -66, -20, -36, 6, 6, 70, 4, -96, 42, -66, -44, -42, 26, 12, -52, 90, 54, -82, -30, 38, -64, -80, -70, 36, -16, -44, -80, -44, -76, 94, -18, 90, -14, 62]],32,36,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],18,23,),
    ([[44, 4, 10, 70, 98, 8, 30, 72, 6, 11, 85, 86, 72, 96, 67, 39, 45, 63, 4, 28, 55, 81, 74, 7, 4, 44, 53, 90, 89, 35, 89, 32, 96, 28, 44, 61, 74, 13, 9, 83, 96, 41], [37, 10, 41, 26, 61, 21, 58, 58, 72, 3, 73, 43, 21, 47, 6, 30, 57, 35, 16, 37, 18, 23, 23, 32, 15, 19, 29, 67, 65, 16, 65, 93, 8, 44, 46, 21, 24, 30, 62, 52, 66, 88], [48, 53, 60, 92, 35, 91, 92, 46, 56, 39, 30, 31, 66, 24, 96, 54, 1, 90, 31, 47, 52, 45, 70, 82, 83, 27, 22, 99, 67, 23, 53, 82, 34, 52, 88, 7, 36, 7, 20, 55, 92, 44], [15, 75, 94, 97, 21, 37, 45, 50, 71, 64, 60, 49, 51, 86, 79, 90, 53, 93, 93, 13, 95, 51, 28, 66, 16, 10, 7, 2, 85, 27, 80, 37, 76, 33, 86, 30, 6, 62, 5, 45, 42, 47], [75, 93, 35, 92, 77, 7, 89, 76, 43, 9, 90, 10, 6, 80, 34, 24, 18, 30, 58, 84, 68, 71, 93, 58, 41, 52, 28, 75, 86, 86, 80, 84, 82, 64, 50, 89, 99, 59, 44, 83, 94, 89], [95, 1, 40, 3, 34, 69, 24, 99, 58, 29, 36, 11, 78, 80, 91, 71, 68, 69, 35, 93, 34, 61, 45, 33, 48, 30, 41, 95, 56, 99, 5, 27, 95, 14, 99, 69, 48, 94, 11, 27, 92, 54], [70, 19, 36, 19, 31, 78, 14, 51, 61, 28, 8, 10, 31, 2, 25, 61, 46, 55, 77, 21, 41, 5, 21, 32, 23, 99, 71, 46, 76, 66, 37, 2, 21, 65, 36, 48, 71, 52, 90, 89, 68, 24], [43, 40, 64, 15, 67, 6, 20, 61, 69, 51, 86, 95, 92, 70, 1, 32, 21, 80, 63, 30, 86, 4, 47, 21, 33, 66, 2, 75, 8, 78, 19, 51, 44, 66, 12, 58, 14, 20, 39, 66, 94, 78], [8, 25, 73, 3, 51, 70, 51, 36, 34, 46, 16, 28, 20, 75, 18, 35, 35, 71, 31, 80, 24, 1, 96, 30, 17, 64, 69, 55, 24, 48, 82, 85, 67, 70, 15, 94, 13, 33, 12, 25, 49, 65], [33, 90, 55, 35, 6, 30, 47, 12, 2, 60, 80, 80, 6, 68, 39, 35, 98, 13, 44, 94, 20, 13, 15, 50, 7, 52, 12, 8, 24, 18, 83, 69, 30, 76, 32, 89, 55, 20, 58, 85, 80, 50], [49, 80, 37, 60, 53, 38, 14, 60, 2, 17, 88, 15, 25, 87, 3, 2, 88, 8, 64, 5, 44, 47, 13, 79, 2, 2, 74, 77, 58, 40, 1, 80, 74, 2, 83, 42, 26, 89, 62, 66, 20, 77], [37, 13, 42, 49, 21, 7, 26, 39, 14, 58, 12, 97, 52, 45, 77, 25, 66, 58, 30, 48, 59, 46, 90, 37, 94, 3, 78, 66, 70, 46, 95, 26, 49, 88, 8, 90, 13, 87, 47, 89, 65, 82], [81, 55, 21, 50, 64, 12, 37, 28, 27, 83, 52, 29, 83, 43, 56, 14, 60, 25, 61, 48, 56, 6, 16, 47, 56, 71, 70, 40, 17, 85, 65, 8, 24, 31, 6, 4, 87, 31, 24, 78, 85, 37], [51, 46, 97, 80, 73, 46, 45, 93, 4, 43, 96, 96, 48, 1, 62, 85, 3, 70, 61, 81, 37, 45, 72, 35, 78, 12, 98, 56, 84, 77, 99, 96, 87, 42, 98, 97, 27, 30, 66, 45, 84, 41], [42, 41, 8, 68, 6, 28, 57, 24, 59, 93, 39, 20, 19, 59, 78, 8, 92, 61, 11, 3, 27, 94, 77, 66, 48, 31, 18, 70, 60, 36, 27, 39, 72, 87, 56, 48, 8, 6, 35, 38, 37, 40], [50, 45, 75, 68, 22, 7, 84, 74, 30, 34, 15, 44, 30, 44, 49, 65, 79, 93, 63, 54, 72, 89, 58, 29, 47, 50, 77, 44, 52, 57, 45, 34, 31, 26, 29, 54, 44, 93, 38, 37, 53, 82], [11, 86, 90, 17, 22, 44, 73, 54, 25, 58, 21, 27, 22, 91, 26, 66, 74, 66, 3, 27, 51, 19, 90, 60, 7, 51, 93, 54, 29, 19, 23, 2, 35, 29, 48, 87, 76, 66, 14, 99, 98, 51], [34, 39, 88, 97, 99, 84, 14, 8, 36, 56, 69, 57, 94, 68, 91, 62, 40, 96, 10, 73, 65, 35, 94, 91, 80, 67, 37, 95, 6, 5, 23, 69, 22, 81, 22, 58, 83, 13, 25, 6, 38, 28], [60, 88, 74, 42, 42, 39, 2, 10, 57, 59, 94, 79, 92, 39, 59, 31, 63, 44, 17, 99, 3, 55, 2, 87, 95, 90, 47, 60, 72, 17, 17, 35, 39, 63, 70, 74, 76, 25, 55, 72, 13, 30], [26, 27, 43, 37, 21, 26, 8, 65, 66, 33, 15, 82, 43, 40, 15, 68, 74, 1, 98, 49, 51, 9, 47, 21, 79, 67, 21, 11, 28, 73, 7, 96, 33, 44, 61, 30, 75, 95, 90, 43, 64, 89], [91, 13, 86, 21, 29, 24, 34, 68, 24, 3, 60, 92, 92, 80, 82, 52, 95, 13, 12, 59, 36, 78, 6, 9, 1, 3, 61, 93, 86, 80, 31, 16, 59, 11, 6, 23, 77, 7, 10, 1, 32, 30], [6, 21, 11, 79, 3, 77, 25, 52, 32, 39, 92, 63, 3, 32, 18, 15, 66, 53, 96, 93, 74, 79, 31, 36, 80, 27, 12, 46, 72, 27, 98, 83, 44, 21, 36, 15, 47, 41, 18, 96, 91, 60], [59, 98, 10, 37, 12, 91, 48, 77, 14, 59, 12, 22, 91, 25, 36, 83, 31, 4, 31, 5, 38, 25, 44, 67, 49, 27, 7, 28, 19, 82, 35, 13, 55, 70, 49, 48, 73, 78, 36, 98, 97, 82], [10, 87, 31, 78, 38, 14, 99, 81, 87, 49, 60, 53, 57, 82, 90, 77, 82, 35, 60, 82, 85, 13, 67, 21, 70, 45, 88, 13, 25, 9, 85, 60, 63, 50, 50, 39, 44, 32, 51, 73, 74, 87], [40, 34, 76, 93, 84, 22, 2, 73, 95, 42, 26, 92, 88, 20, 50, 14, 74, 41, 34, 75, 10, 47, 89, 41, 15, 32, 74, 48, 82, 8, 22, 70, 25, 34, 19, 63, 79, 76, 82, 15, 98, 53], [27, 19, 98, 30, 57, 58, 79, 13, 31, 61, 75, 33, 54, 9, 25, 2, 24, 64, 66, 67, 73, 59, 30, 44, 89, 35, 71, 55, 90, 66, 44, 10, 92, 36, 8, 23, 83, 75, 17, 39, 96, 75], [52, 31, 79, 97, 85, 46, 67, 50, 41, 3, 57, 48, 53, 58, 55, 42, 24, 33, 86, 27, 84, 28, 1, 46, 40, 73, 78, 41, 33, 99, 73, 57, 18, 69, 32, 47, 91, 3, 82, 80, 9, 43], [17, 60, 74, 21, 61, 90, 72, 18, 45, 86, 72, 78, 14, 98, 43, 65, 4, 22, 34, 18, 45, 38, 83, 38, 50, 40, 30, 60, 64, 25, 69, 6, 57, 10, 52, 59, 69, 17, 80, 65, 94, 97], [47, 37, 33, 49, 55, 83, 4, 9, 79, 24, 17, 48, 58, 49, 44, 19, 16, 44, 99, 6, 45, 78, 61, 85, 88, 12, 20, 30, 12, 37, 2, 84, 47, 97, 42, 74, 34, 1, 34, 28, 19, 18], [26, 28, 6, 93, 27, 1, 49, 32, 83, 36, 36, 16, 34, 96, 27, 50, 7, 43, 86, 42, 20, 37, 70, 87, 33, 8, 93, 55, 80, 4, 66, 73, 13, 11, 79, 99, 4, 42, 17, 74, 12, 34], [64, 93, 72, 63, 99, 8, 97, 99, 29, 45, 61, 42, 95, 14, 47, 56, 86, 2, 81, 92, 36, 13, 20, 7, 96, 62, 79, 84, 33, 36, 91, 35, 42, 2, 83, 4, 37, 98, 92, 39, 89, 14], [86, 77, 25, 50, 14, 29, 32, 86, 57, 7, 72, 95, 48, 51, 61, 20, 77, 2, 9, 11, 21, 64, 52, 41, 64, 6, 45, 64, 55, 2, 90, 45, 30, 23, 47, 53, 9, 71, 83, 36, 62, 67], [47, 65, 75, 96, 24, 18, 98, 80, 13, 63, 88, 51, 47, 72, 12, 54, 88, 77, 13, 77, 19, 56, 81, 25, 77, 62, 44, 43, 61, 5, 35, 21, 35, 38, 21, 52, 41, 86, 90, 16, 26, 87], [20, 80, 16, 44, 45, 38, 52, 99, 63, 14, 90, 84, 89, 82, 50, 4, 72, 94, 28, 26, 3, 54, 58, 83, 31, 34, 20, 16, 96, 33, 34, 9, 55, 89, 42, 16, 18, 87, 13, 85, 69, 64], [44, 71, 35, 81, 66, 4, 4, 29, 53, 73, 52, 99, 69, 54, 69, 38, 48, 8, 94, 31, 13, 3, 16, 8, 3, 54, 31, 58, 96, 17, 36, 15, 27, 16, 22, 56, 54, 27, 11, 40, 34, 5], [58, 93, 26, 73, 54, 22, 32, 35, 83, 44, 18, 78, 17, 58, 28, 47, 51, 75, 40, 69, 50, 13, 84, 18, 59, 50, 42, 74, 56, 82, 77, 43, 12, 99, 82, 77, 10, 2, 25, 59, 50, 36], [83, 23, 64, 92, 61, 47, 43, 4, 67, 92, 18, 18, 54, 58, 50, 2, 86, 69, 47, 99, 7, 50, 48, 45, 35, 20, 39, 63, 29, 9, 84, 21, 69, 28, 91, 13, 68, 91, 51, 90, 22, 46], [45, 28, 67, 44, 26, 98, 95, 8, 43, 23, 52, 77, 46, 34, 72, 56, 74, 59, 77, 94, 7, 50, 30, 18, 73, 97, 42, 34, 46, 52, 5, 96, 40, 10, 63, 51, 93, 16, 14, 65, 63, 65], [77, 24, 8, 94, 47, 10, 20, 15, 39, 49, 71, 92, 76, 2, 71, 85, 45, 87, 41, 32, 38, 70, 79, 12, 30, 44, 22, 95, 89, 21, 51, 88, 35, 33, 66, 9, 65, 64, 26, 72, 19, 35], [44, 43, 19, 41, 45, 85, 10, 54, 79, 21, 81, 17, 16, 29, 60, 68, 85, 90, 89, 68, 92, 61, 98, 92, 21, 49, 10, 19, 7, 29, 51, 31, 57, 60, 7, 86, 21, 88, 7, 54, 15, 1], [98, 10, 52, 61, 26, 89, 45, 10, 22, 36, 45, 71, 26, 57, 41, 10, 98, 19, 58, 24, 12, 50, 76, 67, 3, 94, 43, 71, 42, 14, 80, 24, 74, 33, 68, 51, 47, 55, 99, 65, 39, 22], [43, 92, 79, 13, 74, 41, 76, 42, 6, 47, 97, 39, 98, 48, 54, 81, 97, 90, 74, 95, 60, 47, 98, 50, 25, 33, 97, 27, 70, 51, 32, 41, 54, 18, 87, 1, 91, 81, 59, 64, 30, 88]],30,29,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))