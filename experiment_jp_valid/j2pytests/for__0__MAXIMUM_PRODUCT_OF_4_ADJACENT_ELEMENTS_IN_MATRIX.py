# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    max = 0
    for i in range ( n ) :
        for j in range ( n ) :
            if ( ( j - 3 ) >= 0 ) :
                result = ( arr [ i ] [ j ] * arr [ i ] [ j - 1 ] * arr [ i ] [ j - 2 ] * arr [ i ] [ j - 3 ] )
                if ( max < result ) :
                    max = result
            if ( ( i - 3 ) >= 0 ) :
                result = ( arr [ i ] [ j ] * arr [ i - 1 ] [ j ] * arr [ i - 2 ] [ j ] * arr [ i - 3 ] [ j ] )
                if ( max < result ) :
                    max = result
            if ( ( i - 3 ) >= 0 and ( j - 3 ) >= 0 ) :
                result = ( arr [ i ] [ j ] * arr [ i - 1 ] [ j - 1 ] * arr [ i - 2 ] [ j - 2 ] * arr [ i - 3 ] [ j - 3 ] )
                if ( max < result ) :
                    max = result
    return max


#TOFILL
def f_filled (arr, n):
    """ generated source for method FindMaxProduct """
    max = 0
    result = int()
    return max



if __name__ == '__main__':
    param = [
    ([[1, 2, 5, 6, 7, 11, 12, 14, 15, 16, 19, 19, 24, 25, 32, 34, 36, 36, 38, 38, 39, 43, 43, 45, 47, 49, 51, 51, 51, 52, 53, 56, 59, 59, 67, 69, 70, 74, 75, 75, 77, 79, 81, 90, 94, 96, 96, 96], [1, 2, 4, 6, 9, 9, 9, 16, 18, 21, 23, 26, 26, 30, 36, 37, 37, 38, 39, 42, 45, 49, 51, 52, 52, 53, 56, 59, 61, 61, 64, 64, 69, 72, 77, 79, 82, 82, 87, 88, 89, 91, 91, 91, 94, 95, 95, 98], [2, 5, 5, 6, 10, 10, 14, 16, 16, 20, 22, 24, 25, 28, 28, 29, 30, 31, 36, 38, 42, 44, 44, 45, 45, 49, 51, 53, 56, 57, 61, 63, 66, 67, 67, 70, 76, 80, 87, 87, 91, 93, 95, 96, 96, 96, 97, 99], [4, 9, 10, 11, 12, 13, 13, 18, 20, 23, 24, 26, 27, 28, 33, 35, 35, 37, 42, 42, 44, 45, 49, 52, 55, 56, 59, 60, 60, 63, 64, 64, 72, 72, 74, 77, 78, 81, 85, 85, 87, 89, 93, 93, 95, 98, 98, 99], [7, 7, 7, 9, 11, 11, 14, 18, 19, 21, 26, 32, 32, 34, 35, 37, 37, 39, 40, 41, 42, 53, 56, 59, 62, 62, 65, 68, 69, 70, 72, 73, 73, 75, 75, 77, 77, 78, 85, 86, 87, 88, 88, 88, 93, 94, 95, 98], [4, 4, 5, 12, 16, 19, 20, 23, 25, 27, 28, 37, 38, 39, 40, 41, 45, 46, 47, 48, 49, 49, 55, 58, 61, 61, 62, 67, 67, 69, 69, 71, 72, 73, 75, 76, 76, 77, 77, 79, 81, 85, 86, 90, 90, 97, 97, 99], [1, 9, 9, 11, 19, 19, 21, 23, 25, 26, 26, 27, 28, 31, 37, 38, 41, 41, 43, 43, 49, 54, 55, 56, 58, 58, 61, 62, 63, 64, 64, 68, 70, 75, 79, 81, 83, 84, 85, 85, 86, 87, 92, 92, 92, 94, 94, 97], [2, 6, 8, 10, 11, 11, 12, 13, 14, 15, 15, 19, 23, 25, 27, 29, 33, 33, 41, 43, 45, 47, 49, 49, 51, 52, 55, 59, 60, 62, 64, 64, 65, 65, 72, 74, 76, 79, 83, 83, 84, 90, 91, 92, 93, 93, 94, 96], [5, 9, 11, 12, 13, 15, 16, 21, 24, 28, 32, 33, 36, 37, 40, 45, 46, 48, 57, 60, 63, 63, 63, 63, 64, 66, 68, 68, 73, 75, 75, 77, 77, 79, 80, 81, 83, 84, 84, 85, 85, 85, 89, 91, 91, 92, 94, 99], [2, 2, 4, 6, 6, 11, 14, 15, 15, 18, 25, 25, 27, 28, 30, 31, 32, 36, 37, 40, 40, 41, 42, 46, 52, 59, 60, 60, 61, 62, 63, 65, 68, 68, 69, 71, 73, 74, 75, 78, 79, 82, 93, 93, 93, 94, 97, 99], [1, 1, 4, 5, 5, 6, 8, 8, 9, 10, 11, 12, 15, 21, 22, 28, 32, 33, 35, 35, 36, 38, 41, 44, 49, 53, 54, 57, 58, 59, 62, 62, 63, 67, 68, 69, 70, 75, 77, 77, 82, 83, 83, 86, 90, 91, 92, 97], [1, 1, 3, 4, 5, 9, 9, 13, 15, 24, 27, 28, 33, 37, 37, 39, 40, 41, 41, 48, 50, 50, 51, 52, 54, 63, 63, 64, 65, 68, 70, 71, 73, 74, 74, 74, 79, 79, 80, 83, 89, 90, 90, 93, 94, 98, 99, 99], [2, 3, 5, 9, 11, 11, 20, 22, 23, 25, 26, 26, 26, 29, 39, 39, 40, 40, 48, 48, 49, 49, 50, 51, 51, 53, 54, 58, 65, 66, 67, 71, 71, 72, 75, 76, 79, 85, 87, 87, 90, 91, 95, 97, 98, 98, 98, 99], [4, 4, 9, 9, 10, 13, 15, 22, 23, 23, 24, 26, 26, 27, 28, 29, 31, 33, 34, 38, 40, 45, 45, 47, 48, 50, 50, 58, 59, 60, 64, 65, 66, 70, 80, 80, 81, 83, 84, 84, 88, 89, 90, 90, 95, 98, 99, 99], [2, 4, 5, 7, 9, 11, 11, 12, 13, 15, 17, 19, 23, 26, 26, 28, 28, 29, 34, 35, 43, 47, 48, 49, 51, 51, 51, 56, 57, 58, 60, 61, 63, 64, 66, 68, 68, 71, 72, 74, 78, 80, 81, 84, 86, 90, 91, 97], [1, 2, 3, 4, 6, 7, 7, 12, 13, 17, 19, 22, 23, 33, 33, 38, 40, 44, 44, 47, 47, 51, 52, 54, 56, 56, 57, 58, 64, 65, 67, 68, 74, 74, 76, 79, 80, 83, 85, 88, 90, 92, 92, 93, 93, 94, 97, 99], [1, 4, 5, 10, 13, 13, 20, 22, 23, 28, 30, 31, 32, 33, 36, 36, 44, 46, 49, 49, 51, 51, 51, 55, 56, 60, 69, 72, 73, 74, 74, 75, 75, 77, 78, 78, 81, 82, 82, 84, 87, 87, 88, 91, 91, 95, 97, 99], [2, 3, 4, 10, 13, 13, 14, 16, 18, 23, 31, 35, 39, 41, 42, 42, 43, 43, 48, 49, 49, 53, 56, 57, 57, 58, 64, 65, 68, 68, 68, 74, 75, 77, 78, 78, 82, 83, 84, 87, 88, 89, 89, 91, 92, 93, 99, 99], [2, 4, 5, 8, 10, 12, 13, 16, 17, 18, 23, 24, 28, 29, 29, 31, 32, 34, 38, 39, 39, 43, 45, 50, 51, 51, 54, 55, 58, 59, 59, 61, 62, 63, 63, 65, 65, 72, 74, 82, 82, 84, 92, 92, 93, 94, 95, 97], [6, 7, 9, 10, 10, 10, 11, 14, 16, 19, 22, 24, 33, 38, 41, 47, 50, 50, 51, 52, 52, 54, 55, 57, 57, 57, 59, 62, 66, 66, 66, 67, 68, 72, 72, 73, 80, 81, 81, 83, 87, 88, 89, 94, 96, 97, 97, 98], [2, 4, 5, 6, 9, 13, 14, 14, 14, 16, 20, 21, 23, 23, 24, 24, 27, 29, 31, 33, 36, 37, 43, 48, 49, 50, 51, 56, 57, 59, 62, 62, 65, 70, 71, 72, 74, 74, 75, 77, 80, 81, 84, 87, 89, 93, 96, 99], [1, 2, 3, 6, 8, 17, 27, 28, 30, 31, 32, 32, 33, 33, 37, 40, 41, 42, 42, 45, 49, 51, 52, 54, 57, 60, 62, 62, 64, 64, 65, 67, 67, 70, 73, 77, 77, 80, 83, 83, 83, 83, 85, 85, 92, 95, 97, 97], [1, 3, 11, 11, 12, 15, 20, 22, 22, 22, 23, 23, 23, 24, 26, 28, 33, 33, 34, 34, 36, 39, 41, 42, 42, 43, 50, 50, 54, 56, 59, 60, 64, 70, 74, 75, 76, 82, 82, 89, 89, 94, 96, 96, 96, 98, 98, 98], [2, 2, 3, 4, 7, 11, 14, 18, 18, 18, 21, 23, 28, 29, 32, 33, 33, 33, 34, 39, 39, 40, 41, 42, 48, 49, 50, 52, 56, 57, 57, 58, 59, 66, 66, 70, 72, 74, 76, 77, 77, 79, 86, 86, 89, 92, 94, 99], [1, 9, 10, 12, 13, 14, 17, 18, 20, 21, 23, 23, 25, 26, 28, 28, 31, 33, 33, 36, 37, 41, 41, 41, 41, 42, 43, 44, 47, 51, 54, 57, 59, 59, 59, 63, 64, 67, 69, 69, 75, 78, 84, 85, 93, 98, 98, 99], [1, 3, 5, 8, 9, 9, 10, 18, 18, 18, 19, 21, 23, 24, 24, 25, 26, 27, 29, 34, 34, 35, 37, 37, 39, 39, 41, 48, 56, 57, 59, 61, 64, 65, 68, 69, 75, 75, 75, 76, 78, 83, 85, 86, 90, 94, 97, 98], [7, 8, 11, 13, 14, 15, 16, 16, 17, 20, 28, 31, 39, 41, 42, 46, 51, 52, 53, 53, 54, 57, 57, 66, 66, 67, 72, 72, 73, 74, 74, 78, 82, 82, 83, 84, 85, 87, 89, 91, 93, 95, 95, 97, 98, 98, 98, 99], [1, 2, 4, 5, 6, 8, 8, 12, 12, 12, 20, 20, 25, 29, 30, 31, 38, 38, 39, 39, 42, 43, 43, 44, 45, 47, 47, 51, 56, 56, 57, 58, 62, 65, 65, 65, 66, 69, 69, 73, 78, 82, 83, 85, 87, 90, 95, 96], [2, 2, 3, 3, 6, 7, 8, 14, 15, 16, 16, 17, 20, 23, 25, 29, 29, 31, 32, 33, 37, 37, 39, 40, 40, 47, 48, 48, 50, 51, 52, 55, 55, 56, 59, 62, 69, 70, 71, 72, 72, 81, 82, 84, 89, 92, 96, 99], [2, 8, 9, 10, 16, 17, 23, 30, 32, 37, 38, 41, 41, 46, 49, 49, 55, 57, 59, 59, 63, 63, 64, 66, 68, 68, 69, 70, 72, 74, 76, 77, 80, 81, 83, 84, 84, 85, 86, 90, 90, 91, 91, 92, 96, 96, 97, 97], [1, 7, 13, 13, 17, 17, 18, 23, 24, 31, 33, 34, 34, 35, 36, 40, 40, 40, 40, 44, 45, 51, 53, 55, 55, 58, 58, 64, 64, 69, 72, 75, 75, 80, 80, 81, 82, 82, 83, 84, 86, 87, 87, 88, 89, 95, 96, 99], [1, 4, 7, 9, 10, 11, 13, 15, 15, 19, 21, 23, 23, 24, 25, 27, 32, 32, 33, 37, 38, 41, 43, 43, 45, 45, 47, 51, 52, 53, 54, 58, 59, 61, 63, 63, 65, 73, 76, 77, 80, 80, 85, 87, 90, 92, 94, 96], [3, 4, 7, 7, 12, 13, 20, 20, 20, 21, 22, 22, 27, 27, 28, 31, 32, 35, 37, 39, 39, 40, 41, 45, 45, 45, 48, 48, 49, 49, 51, 54, 57, 64, 67, 70, 80, 83, 89, 89, 90, 90, 90, 92, 92, 98, 98, 99], [1, 1, 7, 10, 12, 16, 16, 21, 27, 31, 33, 34, 36, 44, 45, 46, 46, 46, 47, 49, 49, 53, 54, 57, 57, 58, 58, 62, 62, 63, 67, 69, 77, 79, 82, 82, 84, 85, 85, 85, 85, 86, 92, 93, 94, 94, 96, 99], [1, 1, 4, 14, 14, 17, 19, 20, 21, 29, 30, 30, 32, 33, 34, 36, 36, 44, 46, 47, 48, 53, 57, 59, 59, 62, 63, 64, 65, 65, 66, 69, 69, 70, 72, 73, 74, 74, 80, 81, 83, 84, 84, 84, 85, 85, 87, 94], [9, 13, 16, 18, 19, 19, 21, 23, 24, 24, 25, 30, 32, 33, 35, 36, 37, 42, 46, 47, 48, 48, 52, 54, 55, 62, 62, 66, 67, 69, 70, 70, 71, 71, 73, 74, 75, 77, 78, 79, 80, 82, 83, 86, 88, 89, 94, 99], [1, 2, 2, 4, 13, 14, 15, 15, 18, 18, 18, 19, 21, 22, 22, 22, 24, 28, 31, 36, 45, 46, 47, 49, 51, 52, 56, 56, 58, 66, 67, 68, 69, 71, 73, 75, 77, 78, 79, 79, 82, 87, 87, 93, 93, 97, 97, 98], [2, 3, 4, 4, 8, 11, 14, 14, 16, 19, 25, 29, 32, 36, 39, 45, 46, 46, 46, 47, 50, 51, 52, 55, 56, 57, 61, 63, 63, 64, 66, 67, 70, 72, 75, 76, 80, 82, 83, 84, 84, 87, 89, 90, 92, 94, 96, 97], [3, 6, 10, 11, 14, 15, 19, 20, 21, 23, 28, 29, 30, 30, 32, 34, 34, 38, 39, 41, 41, 44, 45, 47, 50, 50, 50, 54, 57, 57, 58, 58, 63, 65, 66, 68, 68, 69, 73, 75, 76, 79, 83, 86, 89, 94, 95, 96], [4, 10, 13, 18, 18, 21, 21, 22, 22, 22, 24, 24, 25, 25, 26, 29, 29, 39, 50, 51, 51, 53, 55, 56, 56, 56, 57, 60, 61, 62, 67, 67, 69, 69, 73, 76, 76, 76, 77, 79, 79, 80, 82, 84, 89, 90, 95, 97], [1, 6, 8, 10, 10, 25, 35, 38, 39, 40, 40, 40, 41, 41, 43, 47, 51, 56, 56, 56, 57, 60, 60, 62, 63, 64, 65, 68, 69, 72, 73, 75, 76, 76, 76, 78, 79, 79, 79, 80, 82, 82, 84, 90, 91, 95, 96, 99], [2, 3, 7, 10, 11, 11, 17, 17, 19, 21, 21, 23, 24, 26, 28, 29, 31, 33, 44, 44, 44, 45, 48, 48, 50, 50, 52, 54, 56, 58, 61, 65, 66, 67, 69, 70, 72, 72, 74, 81, 84, 85, 86, 87, 92, 93, 98, 99], [1, 3, 3, 3, 6, 9, 13, 14, 14, 22, 25, 26, 28, 28, 33, 36, 38, 38, 41, 44, 45, 46, 46, 51, 55, 56, 57, 57, 59, 62, 64, 65, 65, 68, 77, 78, 79, 79, 84, 85, 87, 90, 94, 95, 95, 95, 97, 99], [7, 7, 8, 9, 14, 18, 24, 24, 25, 27, 28, 28, 30, 31, 31, 31, 33, 36, 36, 37, 37, 38, 40, 43, 45, 46, 46, 47, 50, 51, 51, 52, 52, 53, 53, 60, 62, 65, 65, 67, 73, 76, 79, 88, 91, 94, 95, 95], [4, 5, 7, 16, 17, 18, 18, 18, 21, 24, 25, 27, 28, 31, 33, 35, 36, 36, 38, 40, 42, 42, 42, 45, 46, 46, 47, 49, 50, 52, 53, 65, 68, 68, 69, 69, 71, 71, 71, 72, 75, 76, 76, 80, 80, 87, 90, 95], [9, 11, 12, 14, 15, 20, 22, 23, 29, 29, 29, 33, 35, 35, 37, 37, 41, 42, 44, 45, 45, 47, 50, 51, 51, 51, 55, 57, 62, 64, 66, 66, 67, 76, 80, 82, 82, 83, 83, 83, 83, 83, 85, 86, 90, 90, 92, 93], [1, 3, 3, 7, 8, 8, 11, 16, 19, 20, 25, 29, 32, 33, 39, 39, 42, 43, 43, 44, 47, 48, 49, 50, 51, 53, 54, 54, 58, 60, 60, 60, 62, 64, 65, 67, 71, 74, 75, 77, 83, 84, 85, 87, 87, 90, 91, 97], [2, 5, 5, 12, 13, 16, 17, 19, 20, 22, 26, 28, 28, 30, 30, 31, 36, 37, 41, 44, 44, 44, 46, 50, 51, 51, 51, 54, 54, 57, 58, 58, 59, 60, 62, 66, 66, 68, 68, 71, 75, 76, 84, 85, 89, 90, 91, 95]],45,),
    ([[36, 16, 60, 44, 14, -68, -28, -98, 14, -6, 24, 56, 54, 70, 70], [-14, 28, -16, -26, -54, 60, 2, 52, 28, -42, 36, 6, 14, 2, -30], [-26, 56, -60, -6, 24, -36, 76, -52, 20, -54, -22, 38, 90, -2, -70], [62, -70, -50, 18, 62, -34, -74, 66, 30, 64, 6, 94, -72, 58, -82], [30, 28, 6, -38, -40, -98, -14, -80, -84, -20, -8, 12, -90, -26, -48], [-2, 64, -38, -82, -82, -18, -14, -20, 28, 16, -94, -78, -80, -4, 32], [-82, -74, 68, 78, -56, 24, -58, 36, -10, 28, 98, 42, 26, -98, 92], [40, -82, 56, 98, 68, -8, 48, -78, -72, -40, 78, 22, -76, 68, 10], [88, 88, 80, 52, -66, -16, -24, -84, 56, -10, 70, -2, 42, 64, 62], [-76, -52, 70, -10, 24, -46, 62, -98, 28, -78, 58, -10, -76, 40, -98], [-82, -58, -12, -98, -54, -62, -32, 52, 48, 64, 28, 72, -84, 48, -14], [-72, 66, -84, 34, -96, 66, -90, 48, 86, -34, -4, -70, -88, -76, 46], [40, 70, 22, -40, 64, -32, -68, -6, -78, -56, -96, -98, -26, -38, -90], [98, 32, 20, 2, -56, 12, 72, -40, 24, 78, 98, 76, 98, -8, 70], [-30, -34, -34, 46, 18, -48, -96, -12, -60, -90, -50, -64, 12, 60, -94]],8,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],18,),
    ([[43, 44, 74, 24, 47, 58, 43, 11, 78, 61], [93, 7, 12, 81, 39, 13, 50, 62, 27, 87], [27, 9, 63, 68, 8, 83, 44, 22, 83, 2], [70, 73, 44, 15, 37, 38, 42, 21, 20, 75], [72, 43, 56, 93, 92, 73, 34, 9, 28, 38], [4, 83, 97, 56, 44, 89, 92, 51, 82, 68], [55, 51, 72, 78, 65, 66, 10, 13, 71, 85], [97, 15, 49, 86, 56, 56, 92, 84, 98, 73], [89, 44, 19, 45, 74, 7, 76, 60, 42, 34], [65, 47, 3, 34, 46, 97, 98, 78, 19, 57]],8,),
    ([[-88, -82, -70, -46, -44, -18, 12, 38, 66, 90, 96], [-98, -90, -84, -62, -42, -30, -16, 4, 14, 18, 26], [-94, -48, -32, -24, -22, -18, 42, 44, 64, 70, 74], [-94, -60, -58, -56, -40, -34, 2, 18, 32, 76, 96], [-94, -74, -62, -56, -50, -46, -2, 34, 34, 44, 68], [-74, -56, -50, -16, -14, 0, 14, 30, 30, 66, 82], [-80, -78, -60, -56, -46, -32, 4, 8, 14, 42, 54], [-68, -66, -58, -50, -50, -40, -16, -2, 4, 10, 80], [-70, -68, -24, -8, -4, 34, 36, 60, 82, 84, 92], [-90, -62, -60, -54, -6, -6, 10, 10, 14, 52, 66], [-88, -72, -70, -18, -6, 28, 38, 50, 56, 72, 90]],9,),
    ([[0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]],18,),
    ([[8, 14, 19, 21, 33, 35, 37, 40, 44, 49, 52, 68, 68, 72, 77, 80, 86, 88, 88, 99], [10, 12, 18, 18, 25, 27, 30, 32, 32, 42, 46, 47, 48, 53, 67, 69, 70, 84, 85, 89], [12, 15, 18, 24, 26, 33, 41, 45, 55, 71, 73, 79, 82, 87, 88, 88, 89, 91, 92, 98], [1, 1, 11, 16, 24, 24, 27, 42, 49, 50, 69, 69, 72, 73, 75, 80, 80, 82, 95, 96], [1, 6, 12, 13, 14, 22, 28, 30, 39, 51, 53, 66, 68, 68, 69, 77, 86, 90, 96, 99], [2, 6, 24, 26, 28, 32, 32, 37, 38, 54, 56, 61, 64, 64, 68, 71, 71, 76, 79, 86], [22, 31, 32, 34, 39, 47, 54, 57, 59, 61, 62, 72, 72, 74, 79, 79, 80, 85, 91, 93], [3, 7, 12, 13, 15, 16, 21, 26, 26, 36, 56, 60, 62, 63, 64, 66, 67, 71, 76, 83], [3, 22, 29, 30, 34, 35, 36, 39, 41, 42, 43, 51, 57, 58, 72, 72, 80, 84, 88, 92], [9, 14, 17, 29, 34, 37, 38, 39, 40, 46, 46, 52, 62, 68, 77, 78, 79, 92, 93, 95], [1, 17, 17, 18, 19, 23, 26, 27, 36, 37, 48, 53, 56, 62, 62, 68, 69, 78, 78, 84], [20, 20, 22, 33, 33, 33, 43, 48, 60, 63, 64, 70, 77, 80, 80, 85, 87, 88, 91, 94], [7, 10, 10, 13, 14, 14, 23, 42, 64, 65, 65, 72, 73, 74, 75, 76, 77, 78, 79, 91], [1, 4, 9, 12, 13, 13, 23, 23, 27, 33, 34, 34, 37, 40, 43, 63, 67, 70, 87, 96], [1, 2, 8, 11, 12, 14, 14, 23, 24, 33, 44, 45, 47, 55, 78, 79, 83, 98, 98, 99], [3, 9, 18, 21, 24, 28, 34, 35, 45, 46, 59, 60, 60, 63, 64, 84, 95, 96, 97, 97], [4, 11, 17, 19, 20, 20, 20, 30, 31, 41, 45, 47, 64, 68, 76, 81, 83, 89, 93, 93], [2, 8, 10, 21, 38, 40, 43, 44, 47, 52, 55, 71, 75, 80, 85, 85, 89, 92, 94, 99], [3, 7, 13, 14, 27, 28, 29, 30, 44, 47, 50, 53, 55, 64, 64, 75, 79, 86, 98, 99], [10, 10, 10, 16, 17, 33, 44, 52, 53, 57, 59, 64, 65, 74, 75, 76, 80, 87, 90, 90]],15,),
    ([[-78, 34, -74, 16, -10, -10, -14, 28], [-22, -84, 48, -20, 2, 86, 88, -60], [32, 16, 98, 30, -10, 48, 82, 56], [48, -32, -76, -54, 36, 56, 6, 82], [6, -20, 64, 56, 6, -28, 30, -72], [-32, -48, 10, 26, 40, -8, -26, -54], [-68, -36, -86, -12, -6, 62, -90, 26], [-76, 80, 44, -82, 92, -12, -56, -8]],7,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],17,),
    ([[76, 57, 99, 99, 95, 61, 64, 17, 58, 47], [52, 18, 37, 70, 17, 3, 33, 84, 80, 7], [2, 34, 4, 49, 17, 71, 12, 76, 74, 44], [89, 49, 69, 17, 38, 56, 61, 75, 86, 84], [32, 56, 87, 23, 66, 67, 97, 5, 23, 51], [25, 24, 30, 51, 30, 72, 46, 57, 29, 85], [80, 62, 87, 29, 37, 90, 88, 40, 55, 26], [27, 75, 51, 91, 22, 65, 38, 91, 1, 15], [11, 56, 38, 93, 54, 94, 23, 90, 37, 51], [61, 82, 79, 22, 66, 55, 67, 26, 93, 93]],6,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))