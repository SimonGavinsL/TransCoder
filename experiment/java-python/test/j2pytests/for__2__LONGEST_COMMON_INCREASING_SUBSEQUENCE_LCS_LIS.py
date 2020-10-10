# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr1 , n , arr2 , m ) :
    table = [ 0 ] * m
    for j in range ( m ) :
        table [ j ] = 0
    for i in range ( n ) :
        current = 0
        for j in range ( m ) :
            if ( arr1 [ i ] == arr2 [ j ] ) :
                if ( current + 1 > table [ j ] ) :
                    table [ j ] = current + 1
            if ( arr1 [ i ] > arr2 [ j ] ) :
                if ( table [ j ] > current ) :
                    current = table [ j ]
    result = 0
    for i in range ( m ) :
        if ( table [ i ] > result ) :
            result = table [ i ]
    return result


#TOFILL
def f_filled (arr1, n, arr2, m):
    """ generated source for method LCIS """
    table = [None]*m
    result = 0
    return result



if __name__ == '__main__':
    param = [
    ([1, 7, 9, 35, 43, 51, 51, 66, 88],5,[10, 21, 38, 50, 65, 67, 87, 93, 99],8,),
    ([-52, 52, -92, -46, -94, 30, -36, 18, -98, 22, -36, 96, -88, -50, 50],7,[-58, 40, 56, -62, -92, -94, 40, 18, -2, -76, -78, -14, 44, 84, 4],10,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],36,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],22,),
    ([5, 74, 29],1,[57, 33, 48],1,),
    ([-84, -74, -70, -62, -56, -56, -52, -2, 6, 24, 28, 44, 44, 52],8,[-98, -96, -88, -66, -32, -26, -24, -20, -4, 20, 48, 74, 90, 96],12,),
    ([0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],17,[1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],15,),
    ([3, 4, 4, 7, 15, 15, 16, 22, 32, 32, 37, 39, 39, 41, 43, 46, 47, 47, 49, 75, 79, 80, 86, 88, 93],19,[9, 12, 15, 20, 22, 27, 28, 28, 30, 31, 35, 39, 47, 58, 58, 60, 73, 74, 76, 78, 80, 86, 95, 96, 98],14,),
    ([70, -64, 0, 52, 32, -98, 38, -8, 34, 70, 98, 58, -48, -60, -28, -22, -72, 82, -98, -36],16,[-18, 88, -40, -52, 30, -10, -18, -56, 84, -22, -64, 80, -14, -64, 40, 92, 48, -8, 24, 82],12,),
    ([0, 0, 1, 1, 1, 1, 1, 1],7,[0, 1, 1, 1, 1, 1, 1, 1],7,),
    ([46, 87, 98],2,[67, 31, 54],2,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))