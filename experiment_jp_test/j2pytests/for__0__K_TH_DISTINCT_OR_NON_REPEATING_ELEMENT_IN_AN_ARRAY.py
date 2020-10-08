# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n , k ) :
    dist_count = 0
    for i in range ( n ) :
        j = 0
        while j < n :
            if ( i != j and arr [ j ] == arr [ i ] ) :
                break
            j += 1
        if ( j == n ) :
            dist_count += 1
        if ( dist_count == k ) :
            return arr [ i ]
    return - 1


#TOFILL
def f_filled (arr, n, k):
    """ generated source for method printKDistinct """
    dist_count = 0
    return -1



if __name__ == '__main__':
    param = [
    ([2, 3, 8, 18, 20, 33, 53, 56, 60, 71, 76, 80, 81, 87, 88, 89, 92, 95],16,16,),
    ([-78, 6, 32, 52, -12, -32, 22, -40, -82, 24, 30, 10, -40],8,6,),
    ([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],7,5,),
    ([3, 28, 55, 21, 42, 60, 96, 83, 98, 75, 29, 73, 51, 21, 27, 65, 19, 47, 12, 81, 19, 94, 50, 43, 21, 32, 52, 44, 52, 91, 49, 59, 52, 10, 75, 86, 46, 43, 3, 49, 70, 60, 77, 99, 27, 63],40,39,),
    ([-96, -90, -76, -44, -16, -8, 0, 0, 2, 2, 8, 14, 16, 18, 18, 20, 20, 28, 34, 44, 68, 74, 84, 90],23,12,),
    ([0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],10,8,),
    ([3, 4, 5, 8, 9, 15, 26, 26, 26, 35, 39, 40, 42, 43, 45, 45, 48, 52, 54, 56, 57, 67, 74, 77, 79, 80, 81, 86, 87, 92, 95, 97],26,24,),
    ([-76, -24, -12, 66, -40, 26, 72, 46, -56, 58, -68, 2, -82],6,10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],27,17,),
    ([29, 83, 32, 75, 5, 22, 68, 64, 36, 18, 7, 63, 16, 42, 77, 61, 1, 26, 12, 41, 67, 85, 85, 35, 94, 18, 14, 65, 8, 55, 44, 34, 48, 23, 8, 27, 86, 2, 51, 91],28,24,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))