# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( mat , n ) :
    res = 0
    for i in range ( n ) :
        if mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] :
            res = res + 1
    return res


#TOFILL
def f_filled ( mat , n ) :
    res = 0
    for i in range ( n ) :
        if mat [ i ] [ i ] == mat [ i ] [ n - i - 1 ] :
            res += 1
    return res


if __name__ == '__main__':
    param = [
    ([[62]],0,),
    ([[-56, -6, -12, 64, 36, 12, -40, -38, 14, 68, 62, -46, -30], [56, 30, -18, -92, -10, 76, 6, 64, 14, -94, 34, 6, 12], [-80, 90, -40, 2, -48, -28, 58, 86, -14, -50, -78, 36, -96], [-92, 84, -86, 60, -18, 18, 24, -16, 42, 66, -10, -70, 16], [68, 12, 78, 8, -44, 2, -76, 4, 4, 8, 24, -74, -60], [36, -34, 90, -76, 92, 48, -6, -46, 46, 0, -8, -68, 24], [54, -62, 10, 10, 88, 28, -92, -4, -92, -74, 86, -52, 24], [22, 0, 24, 98, 2, 76, -76, -76, 72, 66, -88, 28, 48], [14, 10, 78, 34, -64, 88, 48, -12, -8, 80, -66, -4, -92], [-22, -68, 44, 92, 42, 20, 34, -14, 18, -34, -76, 12, -12], [26, 50, 10, 84, -54, -56, 80, -24, 42, -56, 80, 20, -52], [-2, -98, -46, 34, -22, 2, 18, 2, -80, 70, 26, 38, -98], [-70, 44, -54, -12, 78, -10, -80, 44, -34, 16, -54, 24, -36]],10,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],31,),
    ([[64, 13, 62, 37, 41, 79, 13, 99, 82, 90, 42, 83, 94, 22, 55, 35, 38, 49, 83, 12, 20, 92, 69, 27, 21, 97, 26, 25, 87, 47, 60, 20, 71, 80, 46, 57, 36, 9, 87, 39, 67, 13, 34, 75, 48, 41, 54, 12, 26], [51, 78, 95, 74, 11, 77, 69, 21, 55, 66, 93, 44, 55, 80, 79, 95, 39, 25, 8, 44, 78, 35, 14, 24, 2, 44, 74, 10, 7, 50, 29, 29, 50, 47, 68, 20, 37, 69, 52, 6, 15, 4, 54, 1, 41, 61, 53, 23, 17], [53, 35, 55, 27, 25, 62, 59, 43, 10, 1, 57, 97, 60, 19, 4, 74, 59, 30, 1, 88, 81, 66, 56, 7, 79, 7, 87, 61, 83, 18, 20, 97, 68, 8, 21, 84, 48, 4, 89, 46, 19, 93, 4, 80, 95, 69, 59, 19, 63], [21, 59, 15, 68, 31, 60, 58, 61, 22, 82, 65, 88, 58, 71, 10, 5, 6, 25, 18, 20, 98, 68, 8, 63, 25, 16, 63, 56, 31, 28, 2, 7, 56, 29, 22, 42, 7, 60, 7, 14, 53, 25, 10, 32, 46, 3, 95, 18, 67], [15, 28, 19, 88, 66, 26, 2, 49, 8, 58, 40, 51, 7, 2, 61, 29, 27, 67, 73, 4, 70, 78, 84, 60, 99, 20, 67, 1, 44, 16, 27, 71, 95, 75, 99, 81, 46, 22, 18, 81, 35, 1, 80, 88, 34, 25, 26, 57, 32], [26, 78, 58, 96, 76, 98, 27, 74, 52, 59, 48, 90, 61, 43, 2, 44, 99, 64, 93, 36, 70, 35, 96, 87, 2, 23, 45, 78, 79, 83, 91, 36, 61, 94, 69, 51, 34, 93, 91, 13, 32, 24, 81, 14, 98, 88, 1, 92, 50], [18, 5, 12, 94, 10, 40, 95, 87, 90, 58, 11, 13, 82, 3, 83, 1, 86, 37, 94, 75, 92, 2, 65, 6, 11, 52, 5, 3, 76, 16, 30, 91, 96, 24, 25, 49, 3, 78, 90, 41, 65, 42, 49, 46, 28, 39, 97, 1, 11], [74, 11, 85, 75, 6, 42, 41, 60, 25, 36, 59, 14, 95, 10, 89, 93, 70, 44, 34, 6, 57, 32, 59, 74, 59, 35, 61, 48, 64, 16, 64, 46, 34, 14, 84, 89, 66, 36, 8, 87, 78, 72, 99, 83, 34, 88, 71, 17, 13], [23, 28, 65, 90, 23, 29, 89, 11, 13, 75, 37, 53, 76, 76, 28, 63, 22, 82, 74, 73, 17, 21, 54, 19, 65, 17, 23, 11, 28, 60, 16, 19, 55, 83, 48, 14, 8, 84, 40, 91, 96, 72, 16, 79, 80, 60, 17, 92, 94], [40, 51, 57, 69, 48, 63, 30, 7, 43, 79, 82, 92, 48, 12, 12, 13, 10, 88, 10, 55, 16, 57, 29, 91, 11, 52, 99, 91, 81, 23, 37, 32, 29, 50, 49, 31, 85, 67, 37, 30, 70, 48, 90, 64, 14, 73, 31, 90, 71], [15, 51, 10, 81, 51, 47, 52, 69, 3, 55, 87, 94, 54, 79, 33, 29, 18, 41, 37, 76, 65, 68, 36, 83, 88, 13, 22, 74, 70, 21, 88, 75, 41, 71, 76, 69, 76, 22, 57, 27, 91, 4, 30, 96, 82, 71, 57, 90, 55], [91, 67, 84, 54, 10, 88, 37, 45, 22, 67, 82, 92, 28, 55, 7, 94, 6, 23, 89, 35, 24, 33, 24, 8, 33, 21, 34, 55, 17, 31, 85, 79, 46, 15, 81, 87, 39, 77, 89, 36, 17, 98, 53, 8, 52, 74, 55, 88, 76], [5, 28, 79, 7, 68, 20, 99, 83, 74, 66, 32, 86, 13, 5, 76, 32, 98, 20, 26, 90, 83, 55, 92, 20, 32, 38, 20, 11, 18, 27, 76, 18, 8, 93, 62, 75, 45, 53, 98, 2, 37, 56, 72, 68, 35, 45, 75, 94, 12], [74, 8, 85, 10, 58, 59, 35, 46, 78, 87, 33, 7, 37, 22, 61, 10, 79, 26, 1, 86, 65, 31, 25, 9, 55, 40, 94, 15, 57, 64, 88, 98, 23, 3, 48, 38, 20, 82, 73, 42, 24, 68, 47, 81, 33, 78, 37, 99, 80], [66, 29, 59, 85, 53, 93, 30, 27, 51, 39, 82, 66, 97, 27, 31, 42, 19, 46, 25, 71, 33, 90, 31, 45, 53, 77, 27, 79, 74, 37, 6, 57, 86, 11, 21, 37, 80, 77, 6, 17, 57, 39, 61, 49, 23, 74, 72, 10, 12], [58, 96, 34, 23, 27, 20, 10, 25, 1, 6, 93, 17, 80, 48, 11, 23, 99, 64, 8, 69, 94, 29, 49, 85, 88, 19, 32, 53, 36, 86, 2, 3, 67, 79, 23, 76, 8, 26, 47, 41, 99, 81, 52, 39, 34, 50, 15, 39, 31], [31, 27, 87, 26, 85, 60, 45, 36, 89, 51, 10, 33, 60, 82, 29, 23, 71, 16, 68, 90, 3, 24, 36, 59, 26, 53, 71, 84, 23, 89, 64, 74, 8, 51, 89, 16, 78, 72, 70, 19, 83, 73, 52, 34, 8, 55, 87, 88, 27], [14, 57, 68, 56, 58, 90, 49, 65, 72, 65, 73, 7, 79, 37, 37, 43, 44, 16, 82, 67, 95, 2, 47, 51, 70, 9, 89, 65, 90, 69, 94, 18, 97, 35, 38, 67, 77, 18, 4, 95, 78, 22, 67, 86, 74, 35, 72, 25, 6], [36, 20, 73, 37, 38, 25, 96, 92, 83, 61, 51, 80, 59, 22, 41, 14, 90, 7, 94, 25, 31, 30, 85, 14, 58, 68, 10, 60, 44, 80, 96, 43, 82, 47, 31, 83, 19, 70, 7, 34, 54, 43, 74, 52, 37, 46, 42, 49, 82], [52, 52, 61, 51, 71, 67, 28, 85, 72, 35, 66, 48, 50, 49, 81, 31, 69, 15, 28, 87, 96, 97, 21, 1, 16, 37, 80, 92, 16, 8, 31, 58, 56, 44, 96, 7, 66, 11, 55, 18, 69, 90, 53, 15, 22, 57, 8, 98, 18], [85, 30, 77, 51, 48, 29, 46, 76, 27, 42, 34, 4, 56, 28, 46, 97, 57, 20, 69, 24, 76, 54, 58, 46, 12, 71, 27, 6, 77, 17, 35, 49, 84, 1, 61, 57, 66, 63, 52, 42, 66, 21, 84, 23, 18, 28, 71, 18, 27], [25, 53, 3, 58, 79, 23, 32, 85, 49, 99, 90, 65, 88, 91, 98, 57, 30, 1, 46, 65, 7, 77, 74, 65, 30, 88, 77, 53, 38, 76, 90, 72, 46, 59, 56, 94, 82, 7, 33, 63, 81, 37, 57, 47, 29, 77, 28, 32, 90], [79, 94, 9, 36, 56, 25, 72, 21, 73, 96, 11, 73, 20, 31, 79, 50, 95, 9, 36, 63, 8, 50, 57, 2, 91, 1, 84, 74, 41, 71, 73, 97, 36, 18, 69, 57, 49, 55, 95, 89, 36, 83, 96, 23, 60, 15, 61, 75, 72], [41, 24, 81, 57, 15, 46, 19, 53, 56, 45, 66, 62, 79, 11, 48, 73, 91, 48, 8, 65, 91, 88, 55, 36, 13, 38, 68, 66, 21, 45, 65, 41, 13, 34, 2, 85, 47, 28, 53, 60, 5, 9, 81, 40, 58, 51, 65, 9, 61], [68, 8, 55, 2, 80, 75, 83, 35, 24, 58, 33, 66, 67, 18, 24, 16, 14, 50, 61, 8, 13, 18, 58, 75, 68, 77, 47, 69, 61, 39, 36, 26, 92, 67, 59, 43, 44, 25, 19, 68, 86, 46, 83, 22, 32, 17, 22, 86, 44], [67, 74, 20, 20, 55, 32, 97, 12, 21, 40, 7, 72, 34, 62, 49, 44, 38, 23, 14, 93, 61, 56, 6, 47, 19, 93, 63, 79, 12, 17, 83, 67, 72, 14, 88, 86, 45, 33, 35, 96, 28, 16, 31, 17, 27, 17, 54, 3, 27], [30, 28, 83, 88, 86, 45, 62, 94, 25, 60, 98, 55, 73, 92, 29, 32, 37, 2, 13, 26, 50, 93, 82, 77, 31, 59, 91, 52, 52, 42, 70, 31, 92, 46, 19, 59, 79, 87, 62, 25, 22, 57, 11, 40, 46, 29, 60, 57, 37], [52, 73, 62, 86, 43, 59, 48, 9, 71, 90, 95, 39, 68, 64, 90, 25, 65, 50, 45, 25, 32, 90, 93, 79, 50, 42, 37, 9, 46, 17, 44, 83, 53, 23, 82, 30, 57, 35, 21, 48, 46, 1, 38, 38, 48, 51, 99, 99, 28], [71, 15, 96, 82, 95, 23, 68, 39, 4, 30, 49, 58, 1, 91, 57, 23, 15, 59, 98, 36, 64, 7, 72, 45, 69, 49, 25, 3, 65, 12, 57, 28, 34, 41, 14, 61, 55, 84, 32, 70, 93, 12, 74, 67, 50, 45, 17, 60, 55], [51, 46, 30, 7, 56, 94, 95, 46, 18, 72, 71, 29, 67, 18, 12, 39, 84, 15, 56, 68, 71, 98, 26, 64, 83, 45, 70, 68, 65, 47, 94, 54, 90, 62, 25, 77, 81, 54, 44, 1, 27, 72, 50, 45, 42, 60, 11, 99, 19], [85, 67, 94, 8, 11, 67, 24, 97, 22, 41, 45, 56, 4, 59, 14, 95, 60, 35, 52, 38, 73, 2, 67, 54, 37, 15, 88, 53, 20, 20, 98, 94, 69, 44, 48, 6, 3, 22, 1, 97, 78, 20, 64, 99, 39, 60, 64, 48, 97], [8, 26, 4, 9, 25, 32, 34, 80, 48, 56, 59, 21, 42, 94, 62, 18, 99, 74, 77, 26, 51, 91, 79, 20, 43, 79, 10, 37, 53, 62, 41, 31, 89, 18, 79, 89, 69, 86, 28, 94, 71, 27, 17, 29, 75, 94, 91, 86, 97], [49, 81, 5, 68, 41, 85, 73, 58, 47, 36, 93, 56, 85, 97, 92, 14, 95, 30, 94, 5, 95, 61, 11, 46, 99, 88, 30, 1, 5, 99, 83, 25, 91, 79, 60, 74, 91, 22, 19, 21, 75, 87, 98, 75, 80, 40, 47, 21, 21], [88, 90, 31, 75, 50, 83, 38, 23, 51, 66, 47, 13, 78, 94, 58, 46, 1, 86, 14, 83, 63, 97, 81, 96, 17, 34, 68, 90, 74, 96, 27, 90, 82, 86, 92, 93, 70, 72, 19, 90, 75, 2, 43, 85, 53, 40, 56, 47, 15], [55, 26, 54, 52, 66, 72, 79, 80, 30, 42, 35, 48, 67, 94, 95, 9, 76, 53, 42, 11, 9, 52, 1, 81, 35, 86, 27, 83, 71, 22, 50, 30, 32, 35, 43, 65, 96, 75, 81, 37, 21, 43, 51, 57, 78, 48, 62, 98, 66], [97, 93, 36, 10, 47, 33, 79, 54, 36, 6, 25, 62, 95, 60, 71, 17, 72, 41, 26, 67, 23, 11, 62, 46, 30, 10, 87, 32, 92, 34, 23, 34, 27, 30, 44, 46, 64, 28, 93, 60, 98, 46, 47, 66, 37, 52, 58, 43, 45], [98, 59, 98, 53, 80, 39, 88, 30, 86, 95, 24, 10, 55, 90, 27, 78, 16, 8, 59, 14, 36, 36, 66, 95, 75, 73, 7, 83, 81, 75, 26, 96, 49, 42, 82, 75, 20, 7, 50, 92, 89, 12, 46, 92, 36, 94, 48, 59, 95], [11, 72, 86, 5, 87, 85, 61, 66, 57, 15, 50, 45, 95, 47, 47, 39, 60, 26, 24, 68, 21, 26, 8, 11, 74, 41, 55, 82, 88, 88, 15, 97, 9, 91, 86, 26, 60, 89, 71, 1, 2, 37, 53, 88, 88, 22, 19, 36, 48], [90, 10, 35, 43, 40, 38, 58, 19, 63, 36, 80, 86, 4, 13, 26, 19, 77, 49, 68, 72, 80, 42, 57, 58, 12, 88, 67, 54, 73, 55, 53, 68, 6, 60, 65, 98, 42, 81, 38, 11, 79, 90, 3, 35, 81, 87, 95, 99, 25], [87, 42, 10, 89, 98, 84, 61, 9, 81, 79, 96, 1, 67, 76, 61, 43, 81, 22, 75, 93, 50, 90, 59, 58, 94, 23, 13, 77, 67, 69, 9, 84, 95, 4, 17, 56, 34, 59, 78, 24, 29, 33, 47, 95, 60, 84, 52, 68, 78], [50, 57, 35, 13, 11, 96, 43, 27, 78, 52, 22, 73, 27, 58, 6, 20, 51, 57, 66, 2, 92, 55, 88, 64, 64, 22, 95, 58, 53, 54, 44, 91, 32, 21, 84, 22, 58, 64, 35, 68, 14, 68, 99, 94, 55, 26, 75, 8, 59], [13, 56, 30, 50, 9, 30, 68, 42, 25, 48, 64, 57, 76, 30, 61, 57, 84, 27, 77, 47, 10, 9, 40, 67, 37, 68, 54, 80, 72, 28, 26, 13, 7, 20, 81, 26, 43, 66, 16, 95, 19, 18, 18, 29, 68, 59, 4, 31, 40], [8, 68, 45, 50, 46, 5, 64, 34, 57, 99, 90, 35, 50, 19, 2, 39, 61, 81, 67, 95, 42, 14, 31, 82, 36, 42, 73, 16, 67, 48, 65, 22, 65, 88, 84, 84, 91, 76, 36, 43, 33, 68, 70, 7, 41, 92, 3, 10, 37], [10, 37, 21, 61, 80, 35, 87, 10, 97, 91, 86, 92, 13, 26, 11, 12, 28, 78, 51, 94, 16, 20, 5, 78, 99, 42, 70, 34, 80, 61, 58, 6, 95, 51, 57, 58, 69, 75, 15, 36, 49, 71, 64, 87, 69, 5, 48, 77, 20], [8, 80, 16, 89, 60, 95, 60, 48, 17, 60, 91, 24, 40, 46, 25, 44, 64, 2, 90, 9, 8, 66, 36, 63, 89, 76, 5, 34, 79, 20, 18, 50, 9, 25, 17, 94, 95, 84, 84, 98, 90, 44, 27, 18, 96, 65, 38, 17, 18], [24, 26, 1, 41, 26, 67, 32, 84, 65, 53, 53, 87, 3, 22, 85, 23, 39, 83, 5, 5, 7, 71, 51, 25, 94, 78, 50, 84, 81, 23, 61, 17, 28, 52, 94, 59, 50, 74, 57, 27, 91, 94, 92, 10, 24, 81, 67, 66, 79], [78, 64, 98, 56, 21, 88, 2, 86, 43, 17, 84, 55, 1, 23, 47, 56, 15, 92, 28, 84, 48, 13, 58, 48, 18, 97, 30, 63, 91, 95, 28, 85, 3, 38, 17, 18, 32, 65, 33, 6, 78, 63, 42, 96, 68, 49, 75, 76, 98], [67, 87, 83, 38, 2, 96, 10, 65, 83, 24, 4, 35, 44, 21, 30, 21, 12, 78, 29, 14, 80, 20, 63, 34, 52, 42, 91, 56, 19, 31, 84, 91, 58, 64, 48, 62, 2, 95, 17, 19, 9, 83, 93, 47, 67, 52, 83, 34, 21], [60, 48, 17, 82, 88, 76, 45, 26, 97, 33, 39, 41, 98, 28, 1, 46, 27, 31, 32, 30, 79, 76, 19, 98, 24, 39, 5, 24, 99, 65, 16, 27, 19, 49, 50, 76, 39, 21, 59, 4, 71, 59, 74, 58, 92, 81, 60, 70, 81]],48,),
    ([[18]],0,),
    ([[0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1]],40,),
    ([[3, 15, 34, 40, 66, 69, 71, 88], [6, 14, 42, 43, 51, 52, 58, 72], [14, 15, 17, 21, 78, 80, 87, 93], [7, 15, 19, 20, 25, 31, 68, 69], [1, 3, 6, 68, 83, 83, 86, 97], [17, 30, 52, 54, 58, 79, 81, 83], [1, 32, 43, 48, 70, 80, 93, 97], [3, 5, 12, 47, 49, 52, 74, 78]],4,),
    ([[-56, 56, 12, -42, 38, -78, 22, -30], [-24, -28, -80, -6, 18, -2, 76, -8], [-46, -74, -48, -98, 32, 52, 60, 48], [42, -46, -84, 44, -86, 72, 8, 70], [80, 90, 50, -26, -98, 84, 8, -52], [-78, -46, 26, 2, -30, -20, -8, 18], [98, 42, 62, 74, -30, -18, 26, -42], [90, 34, 12, -88, -60, -92, -10, -60]],4,),
    ([[0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1]],4,),
    ([[14, 22, 81, 76, 33, 79, 91, 2, 42, 5, 11, 94, 9, 49, 25, 93, 44, 25, 71, 66, 25, 30, 57, 55, 25, 10, 76, 34, 90, 55, 54, 41], [93, 50, 13, 70, 93, 30, 5, 44, 65, 70, 82, 31, 88, 11, 8, 95, 27, 52, 93, 35, 35, 72, 49, 59, 54, 51, 63, 50, 22, 53, 33, 54], [69, 1, 38, 60, 78, 26, 48, 16, 32, 82, 74, 80, 74, 84, 13, 58, 46, 84, 84, 39, 16, 84, 20, 81, 10, 52, 32, 33, 28, 23, 64, 52], [87, 97, 97, 85, 72, 28, 33, 38, 78, 93, 82, 50, 33, 89, 11, 93, 18, 73, 82, 22, 13, 40, 45, 64, 13, 1, 41, 27, 35, 58, 40, 86], [59, 71, 95, 38, 59, 97, 86, 84, 17, 52, 61, 37, 24, 40, 99, 88, 91, 51, 7, 32, 30, 2, 61, 64, 65, 1, 97, 86, 78, 22, 67, 10], [60, 60, 50, 9, 15, 68, 42, 35, 11, 9, 91, 9, 60, 94, 99, 34, 46, 21, 12, 92, 67, 19, 74, 90, 96, 16, 32, 25, 40, 21, 78, 84], [88, 44, 57, 46, 1, 48, 15, 91, 85, 47, 52, 57, 82, 37, 28, 88, 35, 85, 66, 17, 88, 69, 91, 46, 44, 38, 20, 39, 27, 44, 47, 94], [32, 54, 58, 78, 33, 70, 52, 98, 49, 13, 25, 57, 99, 36, 93, 42, 96, 30, 56, 66, 43, 8, 17, 47, 67, 5, 97, 66, 65, 90, 97, 8], [32, 37, 20, 6, 56, 42, 36, 49, 56, 66, 91, 37, 3, 50, 56, 80, 49, 80, 57, 11, 68, 32, 76, 92, 45, 27, 63, 28, 21, 74, 31, 80], [32, 82, 42, 52, 68, 46, 3, 65, 48, 75, 32, 30, 62, 55, 70, 31, 81, 80, 78, 71, 40, 20, 96, 20, 91, 38, 69, 42, 4, 63, 21, 54], [91, 99, 6, 10, 30, 30, 98, 73, 48, 33, 58, 75, 52, 55, 65, 4, 78, 28, 90, 18, 30, 97, 69, 34, 64, 6, 64, 83, 5, 26, 77, 51], [70, 13, 73, 23, 38, 63, 40, 51, 18, 60, 37, 12, 52, 49, 68, 45, 24, 3, 82, 73, 66, 96, 22, 92, 29, 86, 66, 21, 6, 41, 56, 97], [42, 55, 69, 3, 21, 42, 44, 8, 69, 86, 41, 65, 62, 40, 21, 56, 92, 40, 60, 91, 9, 66, 32, 3, 16, 97, 36, 10, 56, 36, 65, 51], [43, 69, 10, 87, 94, 30, 21, 13, 89, 38, 57, 50, 55, 31, 10, 36, 79, 66, 71, 4, 29, 90, 72, 24, 24, 84, 2, 97, 84, 46, 5, 50], [14, 5, 93, 73, 7, 57, 29, 7, 13, 53, 19, 20, 15, 69, 4, 61, 20, 89, 4, 91, 84, 91, 11, 41, 67, 51, 20, 22, 26, 57, 82, 12], [44, 36, 65, 68, 45, 48, 92, 98, 39, 93, 30, 50, 75, 13, 22, 6, 61, 60, 74, 78, 62, 14, 51, 88, 17, 47, 49, 36, 41, 28, 8, 77], [73, 28, 20, 71, 44, 84, 58, 40, 44, 12, 8, 16, 70, 36, 34, 3, 89, 24, 15, 23, 19, 53, 67, 81, 5, 31, 37, 91, 63, 9, 12, 58], [67, 39, 73, 31, 31, 45, 71, 71, 56, 93, 60, 77, 73, 3, 12, 67, 71, 54, 81, 41, 60, 31, 94, 96, 43, 65, 99, 95, 14, 17, 48, 78], [95, 64, 57, 19, 83, 76, 74, 47, 80, 60, 90, 72, 21, 67, 66, 67, 34, 53, 86, 79, 2, 83, 76, 66, 19, 66, 86, 82, 82, 25, 1, 86], [3, 8, 21, 55, 35, 37, 20, 66, 21, 2, 12, 74, 68, 86, 46, 23, 35, 68, 35, 8, 64, 19, 6, 3, 14, 71, 68, 66, 8, 74, 34, 6], [32, 21, 43, 18, 61, 11, 88, 4, 99, 59, 40, 33, 86, 95, 44, 52, 97, 40, 31, 72, 86, 86, 20, 54, 77, 56, 77, 52, 88, 76, 58, 4], [41, 62, 38, 39, 75, 54, 52, 17, 7, 28, 72, 57, 26, 44, 85, 79, 37, 99, 39, 9, 47, 4, 28, 27, 6, 6, 87, 66, 83, 42, 19, 11], [53, 31, 97, 12, 33, 12, 98, 18, 68, 15, 40, 40, 19, 77, 20, 37, 20, 42, 95, 75, 84, 86, 50, 86, 34, 91, 74, 50, 20, 30, 56, 39], [4, 98, 74, 96, 97, 90, 64, 40, 45, 77, 34, 1, 15, 21, 74, 21, 51, 15, 42, 19, 53, 95, 48, 22, 2, 86, 35, 21, 70, 51, 99, 72], [71, 12, 90, 92, 38, 43, 40, 8, 51, 65, 79, 16, 5, 39, 75, 95, 2, 62, 50, 46, 44, 97, 15, 14, 81, 65, 71, 17, 69, 44, 41, 90], [79, 53, 94, 59, 58, 8, 50, 44, 73, 12, 33, 62, 90, 57, 98, 46, 32, 38, 16, 62, 53, 48, 49, 56, 17, 26, 95, 42, 85, 83, 12, 48], [43, 86, 56, 15, 13, 92, 83, 55, 85, 61, 53, 27, 16, 24, 42, 1, 95, 42, 20, 83, 46, 90, 46, 67, 58, 55, 32, 84, 40, 19, 7, 28], [70, 21, 57, 89, 23, 71, 62, 51, 44, 78, 23, 22, 43, 83, 86, 73, 96, 82, 52, 74, 45, 37, 46, 54, 23, 87, 59, 77, 96, 83, 94, 44], [65, 73, 74, 45, 55, 37, 84, 64, 29, 35, 86, 13, 14, 38, 28, 94, 39, 91, 6, 66, 28, 96, 74, 48, 93, 71, 95, 91, 25, 33, 97, 28], [26, 99, 94, 14, 64, 28, 5, 9, 26, 31, 36, 88, 56, 60, 10, 56, 6, 74, 48, 93, 13, 22, 99, 43, 35, 13, 46, 52, 79, 34, 87, 16], [90, 21, 62, 63, 17, 14, 78, 40, 64, 35, 46, 92, 68, 49, 1, 91, 90, 8, 60, 52, 34, 81, 73, 62, 75, 16, 33, 40, 1, 61, 88, 75], [10, 61, 27, 86, 2, 14, 32, 60, 68, 75, 21, 85, 49, 78, 99, 75, 53, 79, 16, 55, 83, 70, 7, 8, 86, 83, 48, 34, 73, 5, 69, 56]],24,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))